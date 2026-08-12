# Multi-tool , Generic Purpose Local LLM Agent
getting started with multi-tool, concurrent sub-models LLM agent in constrained resources environment

## Chosen Models 
* Generic Chatter & Tool-Calling Expert : [__Qwen2.5-0.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)
  * .gguf File Download Command Line (_8bit Quantization_) : 
	
	`curl -L -O https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf`

* Code & Math Expert : [__Qwen2.5-Coder-1.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF)
  * .gguf File Download Command Line (_6bit Quantization_) :

	`curl -L -O https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/resolve/main/qwen2.5-coder-1.5b-instruct-q6_k.gguf`

* Vision Based Model : [__Qwen2.5-VL-3B-Instruct-GGUF__](https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF)
  * .gguf File Download Command Line (_4bit Quantization_) :

	`curl -L -O https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF/resolve/main/Qwen2.5-VL-3B-Instruct-Q4_K_M.gguf`

## Starting Server (Models) 

### `kickstart.sh`

Basic script to quickly __start__ or __kill__ the models. 
No status tracking thus brittle, nor resource allocation
 tuning. Basically scaffolding for a fast setup.

### `server_start.py`

** -- work in progress -- **

Python **llama server** managing solution.
Shall allow for model status overview & resource allocation 
tuning.

## Client 

### `ping.py`

Basic python script to ping a model's API port and submit
a simple prompt.

