from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from src.models import get_chat_model
from src.prompts import load_prompt
from src.tools import python_repl


def create_agent() -> CompiledGraph:
    model = get_chat_model()
    return create_react_agent(
        model=model,
        tools=[python_repl],
        prompt=load_prompt("coder"),
        name="coder",
        checkpointer=MemorySaver(),
    )


if __name__ == "__main__":
    from src.tests import test_agent

    agent = create_agent()
    test_agent(agent, "2 的 8 次方是？")
