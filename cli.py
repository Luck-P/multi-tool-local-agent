from orchestrator import boot 
from langchain_core.messages import HumanMessage
import readline 
from pathlib import Path

app = boot() 

dyn_state = {}
prompt: str = ""

print("/q to quit") 
print("/p </path/to/picture> to load an image\n")

while True:
	prompt = input(">>> ")
	if prompt == "/q": break
	if "/p" in prompt:
		print(f"Picture submitted")
		#extracting the picture path 
		pburst = prompt.split(" ")
		tagr = pburst.index("/p")
		pic_path = Path(pburst[tagr+1])
		print(f"location: {pic_path}...") 
		if pic_path.is_file():
			dyn_state = {"pic_path": pic_path}
		else:
			print("-> invalid file path")
			continue
		#cleaning the prompt
		for i in range(2):
			pburst.pop(tagr)
		#rebuilding the prompt string 
		prompt = ' '.join(pburst) 
		
	if prompt == ".history":
		print("history pretty_print() process...")
		for m in dyn_state.get("messages",[]):
			m.pretty_print()
		continue
	#in-convo vs first prompt dynamic state addition
	if "messages" in dyn_state:
		dyn_state["messages"].append(HumanMessage(content=prompt))
	else:
		dyn_state = {"messages": [HumanMessage(content=prompt)]}
		
	dyn_state = app.invoke(dyn_state)
	print(dyn_state["messages"][-1].content) 
	print(f"\nAgent's chosen model: {dyn_state["nextnode"]}")

	

