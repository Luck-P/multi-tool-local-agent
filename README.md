# Multi-tool , Generic Purpose Local LLM Agent
getting started with multi-tool, concurrent sub-models LLM agent in constrained resources environment

## Chosen Models 
* Generic Conversation & Tool-Calling : [__Qwen2.5-1.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF) (___q6_K___)


* Code & Math Expert : [__Qwen2.5-Coder-1.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF) (___q6_K___)

* Vision Based Model : [__Qwen2.5-VL-3B-Instruct-GGUF__](https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF) (___q4_K_M___)
  * Multimodal Projector : [___q8_0 quantization___](https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF/blob/main/mmproj-Qwen2.5-VL-3B-Instruct-Q8_0.gguf)

## Starting Llama-Server / Running Models

### `kickstart.sh`

Basic script to quickly __start__ or __kill__ the models' respective **llama-server** instances. 

* `./kickstart.sh s` >> start all 3 models. 

* `./kickstart.sh k` >> kill all existing **llama-server** instances.

### `server_start.py`

** -- work in progress -- **

Python **llama server** managing solution.
Shall allow for model status overview & resource allocation 
tuning.

## User Interface

### `ping.py`

Basic python script to ping a model's API port and submit
a simple prompt.

### `cli.py`

Basic CLI enabling conversation with the models. Hangles prompts & picture submission (*local path based*).

## Agent Graph 

### `orchestrator.py`

Handling LangChain core logic, LangGraph mesh definition and configuration as well as **base64** image submission processing.

