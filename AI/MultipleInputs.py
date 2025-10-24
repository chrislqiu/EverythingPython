from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    vals: List[int]
    name: str
    res: str

def process_val(state: AgentState) -> AgentState:
    """This func handles multiple inputs"""

    # stores this str into res using the name and vals properties
    state['res'] = f"Hi there {state['name']}! The sum is {sum(state["vals"])}"

    # returning the modified state
    return state

#set the graph using the state
graph = StateGraph(AgentState)

# param1 = a name for the process of the node, param2 = the func/node itself
graph.add_node("process", process_val)

graph.set_entry_point("process")
graph.set_finish_point("process")
app = graph.compile()

"""
with open("process.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
"""

# invoke compiled graph (app in this case)
output = app.invoke({"vals" : [1,2,3,4,5], "name" : "Chris", })