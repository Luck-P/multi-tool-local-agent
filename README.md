# Multi-tool , Generic Purpose Local LLM Agent
getting started with multi-tool, concurrent sub-models LLM agent in constrained resources environment

## Chosen Models 
* Generic Chatter & Tool-Calling Expert : [__Qwen2.5-0.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)
  * .gguf File Download Command Line (_8bit Quantization_) : 
	
	curl -L -O https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf

* Code & Math Expert : [__Qwen2.5-Coder-1.5B-Instruct-GGUF__](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF)
  * .gguf File Download Command Line (_6bit Quantization_) :

	curl -L -O https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/resolve/main/qwen2.5-coder-1.5b-instruct-q6_k.gguf

* Vision Based Model : [__Qwen2.5-VL-3B-Instruct-GGUF__](https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF)
  * .gguf File Download Command Line (_4bit Quantization_) :

	curl -L -O https://huggingface.co/ggml-org/Qwen2.5-VL-3B-Instruct-GGUF/resolve/main/Qwen2.5-VL-3B-Instruct-Q4_K_M.gguf
	
