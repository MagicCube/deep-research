from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.graph import CompiledGraph
from langgraph_supervisor import create_supervisor

from src.models import get_chat_model
from src.prompts import load_prompt

from .coder import create_agent as create_coder_agent
from .planner import create_agent as create_planner_agent
from .researcher import create_agent as create_researcher_agent


def create_agent() -> CompiledGraph:
    planner_agent = create_planner_agent()
    researcher_agent = create_researcher_agent()
    coder_agent = create_coder_agent()

    model = get_chat_model()
    state_graph = create_supervisor(
        agents=[planner_agent, researcher_agent, coder_agent],
        model=model,
        prompt=load_prompt("supervisor"),
        output_mode="last_message",
        supervisor_name="supervisor",
        add_handoff_back_messages=False,
    )
    return state_graph.compile(checkpointer=MemorySaver())
