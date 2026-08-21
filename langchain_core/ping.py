from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, StateGraph, START, END

print("model loading: qwen2.5-0.5B-Instruct...")

llm = ChatOpenAI(
	base_url="http://localhost:8080/v1",
	api_key="trash",
	model="qwen2.5-0.5B-Instruct-GGUF",
	temperature=0.2,
)
print("model loaded successfully")

print("building graph 'builder'...") 
def call_model(state: MessagesState):
	answer = llm.invoke(state["messages"])
	return {"messages": [answer]}

builder = StateGraph(MessagesState)
builder.add_node("agent",call_model)
builder.add_edge(START, "agent") 
builder.add_edge("agent", END) 

graph = builder.compile()
print("'builder' compiled successfully") 

initstate = {"messages": [
	SystemMessage("you are a growing, promising LLM model in its testing phase"),
	HumanMessage("write down simple instructions to prepare a tomato soup")
	]
}

print("graph invoke > starting procedure") 
finalstate = graph.invoke(initstate)

print(finalstate["messages"][-1].content) 
