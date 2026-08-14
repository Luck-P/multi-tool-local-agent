from orchestrator import boot 
from langchain_core.messages import HumanMessage
import readline 

app = boot() 

dyn_state = {}
prompt: str = ""

print("/q to quit\n") 

while True:
	prompt = input(">>> ")
	if prompt == "/q": break
	if prompt == ".history":
		print("history pretty_print() process...")
		for m in dyn_state.get("messages",[]):
			m.pretty_print()
		continue
	if "messages" in dyn_state:
		dyn_state["messages"].append(HumanMessage(content=prompt))
	else:
		dyn_state = {"messages": [HumanMessage(content=prompt)]}
	dyn_state = app.invoke(dyn_state)
	print(dyn_state["messages"][-1].content) 
	print(f"\nAgent's chosen model: {dyn_state["nextnode"]}")

	

