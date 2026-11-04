#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TEN Turn Detector Inference Script

This script provides a simple command-line interface for the TEN Turn Detector,
allowing users to analyze text inputs and determine their conversation state.
"""

import argparse
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="TEN Turn Detector - Analyze conversation states in text inputs"
    )
    parser.add_argument(
        "--system",
        type=str,
        default="",
        help="Optional system prompt to provide context",
    )
    parser.add_argument(
        "--input", type=str, required=True, help="User input text to analyze"
    )
    return parser.parse_args()


def resolve_device():
    """Pick cuda when available, cpu otherwise (#35: CPU-only environments)."""
    return "cuda" if torch.cuda.is_available() else "cpu"


def load_model(model_id):
    """
    Load the TEN Turn Detector model and tokenizer.

    Args:
        model_id: HuggingFace model ID

    Returns:
        tuple: (model, tokenizer)
    """
    device = resolve_device()
    # bf16 needs a GPU; on CPU keep fp32 (bf16 CPU matmul is unsupported on many builds)
    dtype = torch.bfloat16 if device == "cuda" else torch.float32
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, torch_dtype=dtype
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

    model = model.to(device)
    model.eval()

    print(f"Model loaded on {device} (dtype={dtype})")
    return model, tokenizer


def infer(model, tokenizer, system_prompt, user_input):
    """
    Run inference with the TEN Turn Detector.

    Args:
        model: The loaded model
        tokenizer: The loaded tokenizer
        system_prompt: Optional system prompt for context
        user_input: User text to analyze

    Returns:
        str: The detected conversation state
    """
    device = next(model.parameters()).device
    inf_messages = [{"role": "system", "content": system_prompt}] + [
        {"role": "user", "content": user_input}
    ]
    input_ids = tokenizer.apply_chat_template(
        inf_messages, add_generation_prompt=True, return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_new_tokens=1,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    response = outputs[0][input_ids.shape[-1] :]
    output = tokenizer.decode(response, skip_special_tokens=True)
    return output


if __name__ == "__main__":
    # Parse arguments
    args = parse_args()

    # Model ID on HuggingFace
    model_id = "TEN-framework/TEN_Turn_Detection"

    # Load model and tokenizer
    print(f"Loading model from {model_id}...")
    model, tokenizer = load_model(model_id)

    # Run inference
    print(f"Running inference on: '{args.input}'")
    output = infer(model, tokenizer, args.system, args.input)

    # Print results
    print("\nResults:")
    print(f"Input: '{args.input}'")
    print(f"Turn Detection Result: '{output}'")
