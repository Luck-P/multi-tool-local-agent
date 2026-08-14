from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal , Annotated, TypedDict
from langgraph.graph import StateGraph, START, END , add_messages

generic = ChatOpenAI(
	base_url="http://localhost:8080/v1",
	api_key="none",
	model="qwen2.5-0.5b-instruct-gguf",
	temperature=0.2
)

expert = ChatOpenAI(
	base_url="http://localhost:8081/v1",
	api_key="none",
	model="qwen2.5-coder-1.5b-instruct-gguf",
	temperature=0.2
)

vision = ChatOpenAI(
	base_url = "http://localhost:8082/v1",
	api_key="none",
	model="qwen2.5-vl-3B-instruct-gguf",
	temperature=0.2
)

class Route_Structure(BaseModel):
	target: Literal["direct", "math_code", "vision"] = Field( 
		description = "Select the appropriate model to perform the task or answer directly"
	)
	reasoning: str = Field( description="synthetic justification for model choice")

router = generic.with_structured_output(Route_Structure)

class State(TypedDict):
	messages: Annotated[list[BaseMessage], add_messages]
	nextnode: str

def router_node(state: State):
	tool: Route_Structure = router.invoke(state["messages"])
	return {"nextnode": tool.target}

def direct_node(state: State):
	answer = generic.invoke(state["messages"])
	return {"messages": [answer]}

def expert_node(state: State):
	answer = expert.invoke(state["messages"])
	return {"messages": [answer]}

def vision_node(state: State):
	answer = vision.invoke(state["messages"])

#LangGraph building 

workflow = StateGraph(State) 

workflow.add_node("router", router_node) 
workflow.add_node("direct", direct_node) 
workflow.add_node("expert", expert_node) 
workflow.add_node("vision", vision_node) 

#starting edge - always with the router evaluating the tool / model to use 

workflow.add_edge(START, "router") 

#conditional edges 

def router_output(state: State) -> str:
	return state["nextnode"] #returns (pass) the output of the 'router' node 

workflow.add_conditional_edges(
	"router",
	router_output,
		#mapping : state["nextnode"] mapped against actual node label (add_node()s ) 
	{
		"direct": "direct",
		"math_code": "expert",
		"vision": "vision"
	}
)

#closing edges - 
workflow.add_edge("direct", END) 
workflow.add_edge("expert", END) 
workflow.add_edge("vision", END) 

def boot():
	return workflow.compile()

if __name__ == "__main__":
	boot() 


