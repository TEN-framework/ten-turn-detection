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
        help="Optional system prompt to provide context"
    )
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="User input text to analyze"
    )
    return parser.parse_args()

def load_model(model_id):
    """
    Load the TEN Turn Detector model and tokenizer on GPU.
    
    Args:
        model_id: HuggingFace model ID
        
    Returns:
        tuple: (model, tokenizer)
    """
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        trust_remote_code=True,
        torch_dtype=torch.bfloat16
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    
    # Move model to GPU
    model = model.cuda()
    model.eval()
    
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
    inf_messages = [{"role":"system", "content":system_prompt}] + [{"role":"user", "content":user_input}]
    input_ids = tokenizer.apply_chat_template(
        inf_messages, 
        add_generation_prompt=True, 
        return_tensors="pt"
    ).cuda()
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids, 
            max_new_tokens=1, 
            do_sample=True, 
            top_p=0.1, 
            temperature=0.1, 
            pad_token_id=tokenizer.eos_token_id
        )
        
    response = outputs[0][input_ids.shape[-1]:]
    output = tokenizer.decode(response, skip_special_tokens=True)
    return output

if __name__ == "__main__":
    # Parse arguments
    args = parse_args()
    
    # Model ID on HuggingFace
    model_id = 'TEN-framework/TEN_Turn_Detection'
    
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
