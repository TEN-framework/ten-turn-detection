"""Tests for inference.py device handling and decoding (#35).

Runs without downloading the model: load_model/infer are exercised with stubs.
"""

import importlib.util
import sys
import unittest
from unittest.mock import MagicMock, patch

import torch


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
        fake_tok.apply_chat_template.return_value = torch.tensor([[1, 2, 3]])
        fake_tok.decode.return_value = "END_OF_TURN"
        fake_tok.eos_token_id = 0
        out = mod.infer(fake_model, fake_tok, "sys", "hello")
        self.assertEqual(out, "END_OF_TURN")
        # greedy decoding: a state classifier must be deterministic
        self.assertFalse(fake_model.generate.call_args.kwargs.get("do_sample", True))


if __name__ == "__main__":
    unittest.main()
