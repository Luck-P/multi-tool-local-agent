#!/bin/bash

#basic kickstarter for llama-server & docker boot up

GGUF_FOLDER="/home/luck/hfmodels"

case $1 in

	s)
		if ! [ -d ./.logs/ ]; then
			mkdir ./.logs/
		fi 
		llama-server -m $GGUF_FOLDER/qwen2.5-1.5b-instruct-q6_k.gguf -c 4096 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8080 --host 127.0.0.1 -b 512 > ./.logs/qwen2.5-1.5b-instruct 2>&1 & 
		echo "chat model booting..."
		llama-server -m $GGUF_FOLDER/qwen2.5-coder-1.5b-instruct-q6_k.gguf -c 4096 -np 1 -ctk q8_0 -ctv q8_0 -ngl 99 --port 8081 --host 127.0.0.1 -b 512 > ./.logs/qwen2.5-1.5b-coder 2>&1 &
		echo "expert model booting..."
		llama-server -m $GGUF_FOLDER/Qwen2.5-VL-3B-Instruct-Q4_K_M.gguf -c 8192 -np 1 -ctk q8_0 -ctv q8_0 -ngl 28 --port 8082 --host 127.0.0.1 -b 512 --mmproj $GGUF_FOLDER/mmproj-Qwen2.5-VL-3B-Instruct-Q8_0.gguf > ./.logs/qwen2.5-3b-vl 2>&1 &
		echo "vision model booting..."
		;;
	d)
		if ! [ -d ./.logs/ ]; then
			mkdir ./.logs/
		fi 
		docker compose -f ./container/docker-compose.yml up -d > ./.logs/container 2>&1 &
		;;
	k)
		pkill -9 llama-server && echo "llama-server killed"
		docker compose -f ./container/docker-compose.yml down && echo "docker put down"
		if [ -d ./.logs/ ]; then
			rm -rf ./.logs/
		fi
		;;
	*)
		echo "kickstart.sh >"
		echo "s - starting all 3 models" 
		echo "d - starting docker container"
		echo "k - killing llama-server & docker container"
		;;
esac 
