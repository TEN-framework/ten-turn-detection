![TEN Turn Detection banner][ten-turn-detection-banner]

[![Discussion posts](https://img.shields.io/github/discussions/TEN-framework/ten-turn-detection?labelColor=gray&color=%20%23f79009)](https://github.com/TEN-framework/ten-turn-detection/discussions/)
[![Commits](https://img.shields.io/github/commit-activity/m/TEN-framework/ten-turn-detection?labelColor=gray&color=pink)](https://github.com/TEN-framework/ten-turn-detection/graphs/commit-activity)
[![Issues closed](https://img.shields.io/github/issues-search?query=repo%3ATEN-framework%2Ften-turn-detection%20is%3Aclosed&label=issues%20closed&labelColor=gray&color=green)](https://github.com/TEN-framework/ten-turn-detection/issues)
![](https://img.shields.io/github/contributors/ten-framework/ten-turn-detection?color=c4f042&labelColor=gray&style=flat-square)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome!-brightgreen.svg?style=flat-square)](https://github.com/TEN-framework/ten-turn-detection/pulls)
[![GitHub license](https://img.shields.io/badge/License-Apache_2.0_with_certain_conditions-blue.svg?labelColor=%20%23155EEF&color=%20%23528bff)](./LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/TEN-framework/TEN-turn-detection)

[![GitHub watchers](https://img.shields.io/github/watchers/TEN-framework/ten-turn-detection?style=social&label=Watch)](https://GitHub.com/TEN-framework/ten-turn-detection/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/TEN-framework/ten-turn-detection?style=social&label=Fork)](https://GitHub.com/TEN-framework/ten-turn-detection/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/TEN-framework/ten-turn-detection?style=social&label=Star)](https://GitHub.com/TEN-framework/ten-turn-detection/stargazers/?WT.mc_id=academic-105485-koreyst)

<br>

## Table of Contents
- [Welcome to TEN](#welcome-to-ten)
- [Introduction](#introduction)
- [TEN Hugging Face Space](#ten-hugging-face-space)
- [Key Features](#key-features)
- [Prepared Dataset](#prepared-dataset)
- [Detection Performance](#detection-performance)
- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Model Weights](#model-weights)
  - [Inference](#inference)
- [Citation](#citation)
- [TEN Ecosystem](#ten-ecosystem)
- [Ask Questions](#ask-questions)
- [License](#license)

<br>

## Welcome to TEN 

TEN is a collection of open-source projects for building real-time, multimodal conversational voice agents. It includes [ TEN Framework ](https://github.com/ten-framework/ten-framework), [ TEN Turn Detection ](https://github.com/ten-framework/ten-turn-detection), TEN Agent, TMAN Designer, and [ TEN Portal ](https://github.com/ten-framework/portal), all fully open-source. [ TEN VAD ](https://github.com/ten-framework/ten-vad) is not fully open-source yet, but it is open for public use.

<br>

| Community Channel | Purpose |
| ---------------- | ------- |
| [![Follow on X](https://img.shields.io/twitter/follow/TenFramework?logo=X&color=%20%23f5f5f5)](https://twitter.com/intent/follow?screen_name=TenFramework) | Follow TEN Framework on X for updates and announcements |
| [![Follow on LinkedIn](https://custom-icon-badges.demolab.com/badge/LinkedIn-TEN_Framework-0A66C2?logo=linkedin-white&logoColor=fff)](https://www.linkedin.com/company/ten-framework) | Follow TEN Framework on LinkedIn for updates and announcements |
| [![Discord TEN Community](https://dcbadge.vercel.app/api/server/VnPftUzAMJ?&style=flat&theme=light&color=lightgray)](https://discord.gg/VnPftUzAMJ) | Join our Discord community to connect with developers |
| [![Hugging Face Space](https://img.shields.io/badge/Hugging%20Face-TEN%20Framework-yellow?style=flat&logo=huggingface)](https://huggingface.co/TEN-framework) | Join our Hugging Face community to explore our spaces and models |
| [![WeChat](https://img.shields.io/badge/TEN_Framework-WeChat_Group-%2307C160?logo=wechat&labelColor=darkgreen&color=gray)](https://github.com/TEN-framework/ten-agent/discussions/170) | Join our WeChat group for Chinese community discussions |

<br>

> \[!IMPORTANT]
>
> **Star TEN Repositories** ⭐️
>
> Get instant notifications for new releases and updates. Your support helps us grow and improve TEN!

<br>

![TEN star us gif](https://github.com/user-attachments/assets/eeebe996-8c14-4bf7-82ae-f1a1f7e30705)

<br>

## TEN Hugging Face Space

<https://github.com/user-attachments/assets/725a8318-d679-4b17-b9e4-e3dce999b298>

You are more than welcome to [Visit TEN Hugging Face Space](https://huggingface.co/spaces/TEN-framework/ten-agent-demo) to try VAD and Turn Detection together.

## Introduction

**TEN Turn Detection** is an advanced intelligent turn detection model designed specifically for natural and dynamic communication between humans and AI agents. This technology addresses one of the most challenging aspects of human-AI conversation: detecting natural turn-taking cues and enabling contextually-aware interruptions. TEN Turn Detection incorporates deep semantic understanding of conversation context and linguistic patterns to create more natural dialogue with AI.
<div align="center">
  <img src="images/turn_detection.svg" alt="TEN Turn Detection SVG Diagram" width="800"/>
</div>

**TEN Turn Detection** categorizes user's text into three key states:

**finished**: A finished utterance where the user has expressed a complete thought and expects a response. Example: "Hey there I was wondering can you help me with my order"

**wait**: An ambiguous utterance where the system cannot confidently determine if more speech will follow. Example: "This conversation needs to end now"

**unfinished**: A clearly unfinished utterance where the user has momentarily paused but intends to continue speaking. Example: "Hello I have a question about"

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

*wait.txt*: Contains expressions requesting conversation pauses or termination

*unfinished.txt*: Features incomplete dialogue inputs with truncated utterances

*finished.txt*: Provides complete conversational inputs across multiple domains


## Detection Performance

We conducted comprehensive evaluations comparing several open-source models for turn detection using our test dataset:

<div align="center">


| LANGUAGE | MODEL | FINISHED<br>ACCURACY | UNFINISHED<br>ACCURACY | WAIT<br>ACCURACY |
|:--------:|:-----:|:--------------------:|:----------------------:|:----------------:|
| English  | Model A | 59.74% | 86.46% | N/A |
| English  | Model B | 71.61% | 96.88% | N/A |
| English  | **TEN Turn Detection** | **90.64%** | **98.44%** | **91%** |




| LANGUAGE | MODEL | FINISHED<br>ACCURACY | UNFINISHED<br>ACCURACY | WAIT<br>ACCURACY |
|:--------:|:-----:|:--------------------:|:----------------------:|:----------------:|
| Chinese  | Model B | 74.63% | 88.89% | N/A |
| Chinese  | **TEN Turn Detection** | **98.90%** | **92.74%** | **92%** |


</div>

> **Notes:** 
> 1. Model A doesn't support Chinese language processing
> 2. Neither Model A nor Model B support the "WAIT" state detection

## Quick Start

### Installation

```
git clone https://github.com/TEN-framework/ten-turn-detection.git
pip install "transformers>=4.45.0"
pip install "torch>=2.0.0"
```

### Model Weights

The TEN Turn Detection model is available on HuggingFace:
- Model Repository: [TEN-framework/TEN_Turn_Detection](https://huggingface.co/TEN-framework/TEN_Turn_Detection)

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

The inference script accepts command line arguments for user input:

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

## TEN Ecosystem

| Project | Preview |
| ------- | ------- |
| [**🏚️ TEN Framework**][ten-framework-link]<br>TEN is an open-source framework for real-time, multimodal conversational AI.<br><br>![][ten-framework-shield] | ![][ten-framework-banner] |
| [**️🔂 TEN Turn Detection**][ten-turn-detection-link]<br>TEN is for full-duplex dialogue communication.<br><br>![][ten-turn-detection-shield] | ![][ten-turn-detection-banner] |
| [**🔉 TEN VAD**][ten-vad-link]<br>TEN VAD is a low-latency, lightweight and high-performance streaming voice activity detector (VAD).<br><br>![][ten-vad-shield] | ![][ten-vad-banner] |
| [**🎙️ TEN Agent**][ten-agent-link]<br>TEN Agent is a showcase of TEN Framewrok.<br><br> | ![][ten-agent-banner] |
| **🎨 TMAN Designer** <br>TMAN Designer is low/no code option to make a voice agent with easy to use workflow UI.<br><br> | ![][tman-designer-banner] |
| [**📒 TEN Portal**][ten-portal-link]<br>The official site of TEN framework, it has documentation and blog.<br><br>![][ten-portal-shield] | ![][ten-portal-banner] |

<br>

## Ask Questions

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/TEN-framework/TEN-framework)

Most questions can be answered by using DeepWiki, it is fast, intutive to use and supports multiple languages.

<br>

## License 
This project is [ Apache 2.0 licensed with certain conditions.](./LICENSE)

[back-to-top]: https://img.shields.io/badge/-Back_to_top-gray?style=flat-square

[ten-framework-shield]: https://img.shields.io/github/stars/ten-framework/ten_framework?color=ffcb47&labelColor=gray&style=flat-square&logo=github
[ten-framework-banner]: https://github.com/user-attachments/assets/7c8f72d7-3993-4d01-8504-b71578a22944
[ten-framework-link]: https://github.com/ten-framework/ten_framework

[ten-vad-link]: https://github.com/ten-framework/ten-vad
[ten-vad-shield]: https://img.shields.io/github/stars/ten-framework/ten-vad?color=ffcb47&labelColor=gray&style=flat-square&logo=github
[ten-vad-banner]: https://github.com/user-attachments/assets/d45870e4-9453-4047-8163-08737f82863f

[ten-turn-detection-link]: https://github.com/ten-framework/ten-turn-detection
[ten-turn-detection-shield]: https://img.shields.io/github/stars/ten-framework/ten-turn-detection?color=ffcb47&labelColor=gray&style=flat-square&logo=github
[ten-turn-detection-banner]: https://github.com/user-attachments/assets/8d0ec716-5d0e-43e4-ad9a-d97b17305658

[ten-agent-link]: https://github.com/TEN-framework/ten-framework/tree/main/ai_agents
[ten-agent-banner]: https://github.com/user-attachments/assets/38de2207-939b-4702-a0aa-04491f5b5275
[tman-designer-banner]: https://github.com/user-attachments/assets/804c3543-0a47-42b7-b40b-ef32b742fb8f

[ten-portal-link]: https://github.com/ten-framework/portal
[ten-portal-shield]: https://img.shields.io/github/stars/ten-framework/portal?color=ffcb47&labelColor=gray&style=flat-square&logo=github
[ten-portal-banner]: https://github.com/user-attachments/assets/e17d8aaa-5928-45dd-ac71-814928e26a89
