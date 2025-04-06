from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from src.models import get_chat_model
from src.prompts import load_prompt
from src.tests import test_agent
from src.tools import web_crawl, web_search


def create_agent() -> CompiledGraph:
    model = get_chat_model()
    return create_react_agent(
        model=model,
        tools=[web_search, web_crawl],
        prompt=load_prompt("researcher"),
        name="researcher",
        checkpointer=MemorySaver(),
    )


if __name__ == "__main__":
    agent = create_agent()
    test_agent(agent, "字节跳动最新的估值是多少？")
