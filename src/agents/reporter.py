from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from src.models import get_chat_model
from src.prompts import load_prompt


def create_agent() -> CompiledGraph:
    model = get_chat_model()
    return create_react_agent(
        model=model,
        tools=[],
        prompt=load_prompt("reporter"),
        name="reporter",
        checkpointer=MemorySaver(),
    )
