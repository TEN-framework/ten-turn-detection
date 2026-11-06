"""Tests for inference.py device handling and decoding (#35).

Runs without downloading the model: load_model/infer are exercised with stubs.
"""

import importlib.util
import sys
import unittest
from unittest.mock import MagicMock, patch

import torch
from transformers import BatchEncoding


def _load_module():
    spec = importlib.util.spec_from_file_location("ten_inference", "inference.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ten_inference"] = mod
    spec.loader.exec_module(mod)
    return mod


class TestDeviceFallback(unittest.TestCase):
    def test_resolve_device_cpu_when_no_cuda(self):
        mod = _load_module()
        with patch.object(torch.cuda, "is_available", return_value=False):
            self.assertEqual(mod.resolve_device(), "cpu")

    def test_resolve_device_cuda_when_available(self):
        mod = _load_module()
        with patch.object(torch.cuda, "is_available", return_value=True):
            self.assertEqual(mod.resolve_device(), "cuda")

    def test_load_model_uses_fp32_on_cpu(self):
        """bf16 matmul is unsupported on many CPU builds: keep fp32 there."""
        mod = _load_module()
        fake_model = MagicMock()
        fake_model.to.return_value = fake_model  # nn.Module.to returns self
        fake_tok = MagicMock()
        with (
            patch.object(torch.cuda, "is_available", return_value=False),
            patch(
                "ten_inference.AutoModelForCausalLM.from_pretrained",
                return_value=fake_model,
            ) as m_load,
            patch("ten_inference.AutoTokenizer.from_pretrained", return_value=fake_tok),
        ):
            model, tok = mod.load_model("stub/model")
        self.assertIs(model, fake_model)
        self.assertIs(tok, fake_tok)
        self.assertEqual(m_load.call_args.kwargs["torch_dtype"], torch.float32)
        fake_model.to.assert_called_once_with("cpu")
        fake_model.eval.assert_called_once()

    def test_infer_moves_inputs_to_model_device(self):
        """The device comes from the model, not from a hardcoded .cuda()."""
        mod = _load_module()
        fake_model = MagicMock()
        fake_model.parameters.return_value = iter(
            [MagicMock(device=torch.device("cpu"))]
        )
        fake_model.generate.return_value = torch.tensor([[0, 5]])
        fake_tok = MagicMock()
        fake_tok.apply_chat_template.return_value = BatchEncoding(
            {"input_ids": torch.tensor([[1, 2, 3]])}
        )
        fake_tok.decode.return_value = "END_OF_TURN"
        fake_tok.eos_token_id = 0
        out = mod.infer(fake_model, fake_tok, "sys", "hello")
        self.assertEqual(out, "END_OF_TURN")
        # greedy decoding: a state classifier must be deterministic
        self.assertFalse(fake_model.generate.call_args.kwargs.get("do_sample", True))


class _FakeTokenizer:
    """Mimics apply_chat_template: transformers 5 returns a BatchEncoding by
    default (return_dict=True), transformers 4 returns the input_ids tensor."""

    eos_token_id = 0

    def __init__(self, return_dict_default):
        self.return_dict_default = return_dict_default

    def apply_chat_template(
        self, messages, add_generation_prompt=False, return_tensors=None, **kwargs
    ):
        input_ids = torch.tensor([[1, 2, 3]])
        if kwargs.get("return_dict", self.return_dict_default):
            return BatchEncoding(
                {"input_ids": input_ids, "attention_mask": torch.ones_like(input_ids)}
            )
        return input_ids

    def decode(self, token_ids, skip_special_tokens=False):
        return {7: "finished"}[int(token_ids[0])]


class _FakeModel:
    """Follows the generate() contract: input_ids must be a tensor, the
    prompt is echoed back followed by the new token."""

    def __init__(self):
        self.generate_kwargs = None

    def parameters(self):
        return iter([torch.zeros(1)])

    def generate(self, input_ids=None, **kwargs):
        assert isinstance(input_ids, torch.Tensor), type(input_ids)
        self.generate_kwargs = kwargs
        return torch.cat([input_ids, torch.tensor([[7]])], dim=-1)


class TestChatTemplateOutput(unittest.TestCase):
    def test_infer_with_transformers_5_chat_template(self):
        """transformers>=5 returns a BatchEncoding from apply_chat_template."""
        mod = _load_module()
        model = _FakeModel()
        out = mod.infer(model, _FakeTokenizer(return_dict_default=True), "", "hi")
        self.assertEqual(out, "finished")
        self.assertIn("attention_mask", model.generate_kwargs)

    def test_infer_with_transformers_4_chat_template(self):
        mod = _load_module()
        model = _FakeModel()
        out = mod.infer(model, _FakeTokenizer(return_dict_default=False), "", "hi")
        self.assertEqual(out, "finished")


if __name__ == "__main__":
    unittest.main()
