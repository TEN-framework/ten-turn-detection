# *TEN Turn Detection*
***Turn detection for full-duplex dialogue communication***

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Prepared Dataset](#prepared-dataset)
- [Detection Performance](#detection-performance)
- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Model Weights](#model-weights)
    - [Downloading Model Weights](#downloading-model-weights)
  - [Inference](#inference)
- [Citation](#citation)
- [License](#license)

## Introduction

TEN Turn Detection is an advanced intelligent turn detection model designed specifically for natural and dynamic communication between humans and AI agents. This technology addresses one of the most challenging aspects of human-AI conversation: detecting natural turn-taking cues and enabling contextually-aware interruptions. TEN incorporates deep semantic understanding of conversation context, rhythm, intonation, and linguistic patterns to create more natural dialogue with AI.
<div align="center">
  <img src="images/turn_detection.svg" alt="TEN Turn Detection SVG Diagram" width="800"/>
</div>

TEN Turn Detection categorizes user's text into three key states:

Finished: A finished utterance where the user has expressed a complete thought and expects a response. Example: "Hey there I was wondering can you help me with my order"

Wait: An ambiguous utterance where the system cannot confidently determine if more speech will follow. Example: "This conversation needs to end now"

Unfinished: A clearly unfinished utterance where the user has momentarily paused but intends to continue speaking. Example: "Hello I have a question about"

These three classification states allow the TEN system to create natural conversation dynamics by intelligently managing turn-taking, reducing awkward interruptions while maintaining conversation flow.

TEN Turn Detection utilizes a multi-layered approach based on the transformer-based language model(Qwen2.5-7B) for semantic analysis.

## Key Features

- **Context-Aware Turn Management**
TEN Turn Detection analyzes linguistic patterns and semantic context to accurately identify turn completion points. This capability enables intelligent interruption handling, allowing the system to determine when interruptions are contextually appropriate while maintaining natural conversation flow across various dialogue scenarios.

- **Multilingual Turn Detection Support**
TEN Turn Detection provides comprehensive support for both English and Chinese languages. It is engineered to accurately identify turn-taking cues and completion signals across multilingual conversations.

- **Superior Performance**
Compared with multiple open-source solutions, TEN achieves superior performance across all metrics on our publicly available test dataset.

## Prepared Dataset
We have open-sourced the TEN-Turn-Detection TestSet, a bilingual (Chinese and English) collection of conversational inputs specifically designed to evaluate turn detection capabilities in AI dialogue systems. The dataset consists of three distinct components:

wait.txt: Contains expressions requesting conversation pauses or termination

unfinished.txt: Features incomplete dialogue inputs with truncated utterances

finished.txt: Provides complete conversational inputs across multiple domains


## Detection Performance

We conducted comprehensive evaluations comparing several open-source models for turn detection using our test dataset:

<div align="center">


| LANGUAGE | MODEL | FINISHED<br>ACCURACY | UNFINISHED<br>ACCURACY | WAIT<br>ACCURACY |
|:--------:|:-----:|:--------------------:|:----------------------:|:----------------:|
| English  | Model A | **59.74%** | **86.46%** | *N/A* |
| English  | Model B | **71.61%** | **96.88%** | *N/A* |
| English  | **TEN Turn Detection** | **90.64%** | **98.44%** | **91%** |




| LANGUAGE | MODEL | FINISHED<br>ACCURACY | UNFINISHED<br>ACCURACY | WAIT<br>ACCURACY |
|:--------:|:-----:|:--------------------:|:----------------------:|:----------------:|
| Chinese  | Model B | **74.63%** | **88.89%** | *N/A* |
| Chinese  | **TEN Turn Detection** | **98.90%** | **92.74%** | **92%** |


</div>

> **Notes:** 
> 1. Model A doesn't support Chinese language processing
> 2. Neither Model A nor Model B support the "WAIT" state detection

## Quick Start

### Installation

```
git clone https://github.com/TEN-framework/ten-turn-detection.git

transformers>=4.30.0
torch>=2.0.0
```

### Model Weights

The TEN Turn Detection model is available on HuggingFace:
- Model Repository: [TEN-framework/TEN_Turn_Detection](https://huggingface.co/TEN-framework/TEN_Turn_Detection)

#### Downloading Model Weights

You can download the model in several ways:

1. **Automatic download** (recommended): The model weights will be automatically downloaded when you run the inference script for the first time. HuggingFace Transformers will cache the model locally.

2. **Using Git LFS**:
    ```bash
    # Install Git LFS if you haven't already
    git lfs install

    # Clone the repository with model weights
    git clone https://huggingface.co/TEN-framework/TEN_Turn_Detection
    ```

3. **Using the Hugging Face Hub library**:
    ```python
    from huggingface_hub import snapshot_download

    snapshot_download(repo_id="TEN-framework/TEN_Turn_Detection")
    ```

### Inference

The inference script accepts command line arguments for system prompt and user input:

```
# Basic usage
python inference.py --input "Your text to analyze"

```

Example output:
```
Loading model from TEN-framework/TEN_Turn_Detection...
Running inference on: 'Hello I have a question about'

Results:
Input: 'Hello I have a question about'
Turn Detection Result: 'unfinished'
```

## Citation
If you use TEN Turn Detection in your research or applications, please cite:

```
@misc{TEN_Turn_Detection,
author = {TEN Team},
title = {TEN Turn Detection: Turn detection for full-duplex dialogue communication 

},
year = {2025},
url = {https://github.com/TEN-framework/ten-turn-detection},
}
```
## License 
This project is Apache 2.0 licensed.


