import json 
from pathlib import Path
import subprocess
import psutil


GGUF_PATH = Path("/home/luck/hfmodels/")
SERVERSTATE = "./sstate.json"

class ServerModel:

	def __init__(
		self,
		name: str,
		filename: str,
		port: int, 
		host: str = "127.0.0.1",
		ngl: int = 99,
		context: int = 4096,
		ctk: str = "q8_0",
		ctv: str = "q8_0",
		np: int = 1,
	):
		self.name = name
		self.filename = filename
		self.port = port
		self.host = host 
		self.ngl = ngl
		self.context = context
		self.ctk = ctk
		self.ctv = ctv
		self.np = np

		self.pid: optionnal[int] = None
		self.cdate: optionnal[float] = None

	def starting():
		if self.livecheck() == True :
			print(f" {self.name} running already as PID {self.pid} on {self.port}")
			return
		cmd = [
			"llama-server",
			"-m", str(GGUF_PATH / self.filename),
			"--port", str(self.port),
			"--host", self.host, 
			"-c", str(self.context),
			"-ngl", str(self.ngl),
			"-ctk", self.ctk,
			"-ctv", self.ctv
		]
		print(f"Starting subprocess {self.name}...")
		sphandle = psutil.Popen(cmd)
		self.pid = sphandle.pid
		self.
		print(f"PID : {self.pid}\nCreation Timestamp : ")

	def livecheck():
		

if __name__=="__main__":
	chatl = {
		"fname": "qwen2.5-0.5B-instruct-q8_0.gguf",
		"gpulayers": 99,
		"context": 4096,
		"keyq": "q8_0",
		"valueq": "q8_0"
	}
	expert = {
		"fname": "qwen2.5-coder-1.5B-instruct-q6_k.gguf",
		"gpulayers": 99, 
		"context": 8192,
		"keyq": "q8_0",
		"valueq": "q8_0"
	}
