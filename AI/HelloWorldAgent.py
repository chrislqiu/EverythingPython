from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

# shared data structure that keeps track of info, state schema
class AgentState(TypedDict):
    msg : str

# pass in the state and output the updated state 
def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds greeting message to the state"""
    state['msg'] = "Hey" + state['msg'] + ", how is your day going?"

    return state

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

with open("greetingGraph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())