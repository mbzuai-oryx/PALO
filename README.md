# 🌍 PALO: A Polyglot Large Multimodal Model for 5B People

<p align="center">
    <img src="https://i.imgur.com/waxVImv.png" alt="Oryx Video-ChatGPT">
</p>

Vision-language conversation in English, Chinese, French, Spanish, Russian, Japanese, Arabic, Hindi, Bengali and Urdu

[![Demo](https://img.shields.io/badge/Online-Demo-red)](https://palo.mbzuai-oryx.ngrok.app)
[![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/comming.soon)

---

## 📢 Latest Updates
- **Feb-23-24**- PALO paper and online demo are released. Code, pretrained models and training/evaluation scripts are coming soon!

---

## Overview

In pursuit of more inclusive Vision-Language Models (VLMs), this study introduces a Large Multilingual Multimodal Model called \textsc{Palo}. \textsc{Palo} offers visual reasoning capabilities in 10 major languages, including English, Chinese, Hindi, Spanish, French, Arabic, Bengali, Russian, Urdu, and Japanese, that span a total of $\sim$5B people (65\% of the world population). Our approach involves a semi-automated translation approach to adapt the multimodal instruction dataset from English to the target languages using a fine-tuned Large Language Model, thereby ensuring high linguistic fidelity while allowing scalability due to minimal manual effort. 
The incorporation of diverse instruction sets helps us boost overall performance across multiple languages especially those that are underrepresented like Hindi, Arabic, Bengali, and Urdu. The resulting models are trained across three scales (1.7B, 7B and 13B parameters) to show the generalization and scalability where we observe substantial improvements compared to strong baselines. We also propose the first multilingual multimodal benchmark for the forthcoming approaches to evaluate their vision-language reasoning capabilities across languages.

## 🏆 Contributions
1. We develop Palo: the first multilingual Large Multimodal Model (LMM) covering ten major languages, facilitating vision-language reasoning through a generic model capable of generating responses in any of the ten languages.
2. We assemble an extensive multilingual (10 languages) instruction-tuning dataset, through a critical analysis and subsequent refinement of a state-of-the-art Large Language Model’s target language translations. This dataset is pivotal in improving proficiency in processing and generating content that is linguistically precise across multiple languages.
3. We enhance the multilingual performance of state-of-the-art LMMs~\cite{liu2023llava,chu2023mobilevlm}  across three distinct scales i.e., 1.7B, 7B, and 13B parameters to demonstrate the scalability of our training pipeline. The resulting polyglot LMMs demonstrate performance gains on diverse language tasks with substantial improvements in understanding and generating content for low-resource languages, e.g., Hindi, Arabic, Bengali, and Urdu, without compromising its high-performance on high-resource languages e.g., English, Chinese, French, and Spanish.


#### Stay tuned for the updates!
