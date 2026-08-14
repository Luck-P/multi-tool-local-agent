from orchestrator import boot 
from langchain_core.messages import HumanMessage

app = boot() 

prompt: str = ""

print("/q to quit\n") 

while prompt != "/quit":
	prompt = input(">>> ")
	dyn_state = {"messages": [HumanMessage(content=prompt)]}
	print(dyn_state["messages"][-1].content) 

