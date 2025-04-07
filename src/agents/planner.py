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
        prompt=load_prompt("planner"),
        name="planner",
        checkpointer=MemorySaver(),
    )


if __name__ == "__main__":
    from src.tests import test_agent

    agent = create_agent()
    test_agent(
        agent,
        "查找世界上最高的建筑物的名称和高度，并计算它比一个217米高的建筑物高出多少倍。",
    )
