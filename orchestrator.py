from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal , Annotated, TypedDict, Optional
from langgraph.graph import StateGraph, START, END , add_messages
#picture processing
import base64
import filetype

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

#encoding picture

def pic_encoding(path: str):
	print("encoding picture...")
	with open(path, "rb") as pobj:
		pic = pobj.read()
		print("picture data read correctly...")
		picmime = filetype.guess(pic).mime
		if not picmime:
			return False
		return f"data:{picmime};base64,{base64.b64encode(pic).decode('utf-8')}"
		#return (picmime,base64.b64encode(pic).decode('utf-8'))
	#directly generates the OpenAI protocol-expected image url 
	


class Route_Structure(BaseModel):
	target: Literal["direct", "math_code"] = Field( 
		description = (
		"Select the appropriate option to perform the task"
		"direct > for trivial and conversational tasks"
		"math_code > for calculation or programmation tasks"
		)
	)
	reasoning: str = Field( description="synthetic justification for model choice")

router = generic.with_structured_output(Route_Structure)

class State(TypedDict):
	messages: Annotated[list[BaseMessage], add_messages]
	pic_path: Optional[str]
	nextnode: str

def router_node(state: State):
	m_payload = list(state["messages"])
	if state.get("pic_path"):
		print("router node - picture acknowledged") 
		nn_val = "vision"
	else:
		tool: Route_Structure = router.invoke(m_payload)
		nn_val = tool.target
	return {"nextnode": nn_val}

def direct_node(state: State):
	answer = generic.invoke(state["messages"])
	return {"messages": [answer]}

def expert_node(state: State):
	answer = expert.invoke(state["messages"])
	return {"messages": [answer]}

def vision_node(state: State):
	if not state.get("pic_path"): 	
		print("vision node failure...") 
	pic_url = pic_encoding(state["pic_path"])
	print(f"picture encoded as url {pic_url[:50]}...")
	payload = [HumanMessage(
		content=[
		{"type": "text", "text": state["messages"][-1].content},
		{"type": "image_url", "image_url": {"url": pic_url} }
		]
	)]
	answer = vision.invoke(payload)
	return {"messages": [answer]}

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

#closing edges
workflow.add_edge("direct", END) 
workflow.add_edge("expert", END) 
workflow.add_edge("vision", END) 

def boot():
	return workflow.compile()

if __name__ == "__main__":
	boot() 


