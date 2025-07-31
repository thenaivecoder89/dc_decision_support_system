# dc_decision_support_system
A rule-based decision support system that uses the mistral:7b-instruct-q5_K_M model to generate recommendation reports for DC assessors.
This repository contains a full-stack application designed to assist evaluators in assessing the **Global Expansion Strategy** of organizations based on both **quantitative metrics** and **qualitative documentation**. The system integrates rule-based logic, local LLM inference, and a PostgreSQL database, all wrapped in a modern, intuitive UI.

---

## Purpose

The platform serves as a **decision support system** that:
- Ingests participant-submitted data and documents
- Applies benchmarking rules and rubric logic
- Leverages a locally hosted **quantized Mistral-7B-Instruct model** to generate explanation-based scoring rationales
- Records and manages evaluations in a structured PostgreSQL database
- Presents a clean, user-friendly React frontend for interaction and oversight

---

### Model download and installation instructions

- Navigate to: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF? and download the 8-bit quantized model from the link.
- Once downloaded, download and install the following (if not already available):
  - Visual Studio Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/ and make sure that **Desktop development with C++** and **CMake tools for Windows** are checked post installation. If not, please modify the installation.
  - CUDA Toolkit from https://developer.nvidia.com/cuda-downloads
  - CMake from https://cmake.org/download/ and make sure **Add CMake to Environment PATH** is checked during installation.
- Post installation of the above, run the following bash commands to make sure all pre-requisites are installed:
  - cmake --version
  - nvcc --version
  - git --version
- Once all pre-requisites are installed and checked, clone the llama-cpp-python git using the following command:
  - git clone https://github.com/abetlen/llama-cpp-python.git
  - Once the cloning is done, ensure that CMakeLists.txt is available in llama-cpp-python.
- Once the above git repo is cloned, navigate to llama-cpp-python (from the terminal) and run the following commands:
  - $env:CUDA_PATH="C:\Progra~1\NVIDIA~1\CUDA\v12.9" (if CUDA version is something else, please change accordingly) {this needs to be executed only if first run of the following commands go into error}.
  - $env:CMAKE_ARGS="-DLLAMA_CUDA=on" OR $env:CMAKE_ARGS='-DLLAMA_CUDA=on -DCMAKE_CUDA_HOST_COMPILER="C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\bin\HostX64\x64\cl.exe"'
  - $env:FORCE_CMAKE=1
  - pip install . --no-cache-dir --upgrade --force-reinstall --verbose

---
## Tech Stack



---

### Architecture



---

### Terms of usage

This repository is published for demonstration purposes only. All rights reserved. Unauthorized use, distribution, or replication of any part of this software is strictly prohibited.

---
