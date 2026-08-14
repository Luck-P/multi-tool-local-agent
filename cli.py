from orchestrator import boot 
from langchain_core.messages import HumanMessage

app = boot() 

prompt: str = ""

print("/q to quit\n") 

while True:
	prompt = input(">>> ")
	if prompt == "/q": break
	dyn_state = {"messages": [HumanMessage(content=prompt)]}
	dyn_state = app.invoke(dyn_state)
	print(dyn_state["messages"][-1].content) 

	

