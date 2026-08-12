#!/bin/bash

#basic kickstarter for llama-server boot up

GGUF_FOLDER="/home/luck/hfmodels"

case $1 in

	s)
		llama-server -m $GGUF_FOLDER/qwen2.5-0.5b-instruct-q8_0.gguf -c 4096 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8080 --host 127.0.0.1 & 
		echo "chat model booting..."
		llama-server -m $GGUF_FOLDER/qwen2.5-coder-1.5b-instruct-q6_k.gguf -c 8192 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8081 --host 127.0.0.1 &
		echo "expert model booting..."
		llama-server -m $GGUF_FOLDER/Qwen2.5-VL-3B-Instruct-Q4_K_M.gguf -c 4096 -np 1 -ctk q8_0 -ctk q8_0 -ngl 28 --port 8082 --host 127.0.0.1 &
		echo "vision model booting..."
		;;
	k)
		pkill -9 llama-server
		echo "llama-server killed"
		;;
	bs) 

		llama-server -m $GGUF_FOLDER/qwen2.5-0.5b-instruct-q8_0.gguf -c 4096 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8080 --host 127.0.0.1 & 
		echo "chat model booting..."
		llama-server -m $GGUF_FOLDER/qwen2.5-coder-1.5b-instruct-q6_k.gguf -c 8192 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8081 --host 127.0.0.1 &
		echo "expert model booting..."
		;;

	*)
		echo "kickstart >"
		echo "s - starting all 3 models" 
		echo "k - killing  all   models"
	       	echo "bs- chat + expert standalone start"	
		;;
esac 
