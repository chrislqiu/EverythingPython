from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

# shared data structure that keeps track of info, state schema
class AgentState(TypedDict):
    msg : str

# pass in the state and output the updated state 
def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds greeting message to the state"""
    state['msg'] = "Hey " + state['msg'] + ", how is your day going?"

    return state

# setting the state for the graph
graph = StateGraph(AgentState)

# adding node
graph.add_node("greeter", greeting_node)

# creating entry and finish point
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

# compile graph
app = graph.compile()

"""
with open("greetingGraph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
"""

result = app.invoke({"msg": "Bob"})

print(result["msg"])