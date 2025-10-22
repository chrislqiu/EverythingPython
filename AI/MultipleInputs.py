from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    vals: List[int]
    name: str
    res: str

def process_val(state: AgentState) -> AgentState:
    """This func handles multiple inputs"""

    