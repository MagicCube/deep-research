from langgraph.graph.graph import CompiledGraph


def test_agent(agent: CompiledGraph, initial_message: str):
    for chunk in agent.stream(
        {
            "messages": [
                initial_message,
            ]
        },
        stream_mode="values",
        config={"configurable": {"user_id": "1", "thread_id": "1"}},
    ):
        messages = chunk["messages"]
        last_message = messages[-1]
        last_message.pretty_print()
        print("\n\n")


def test_multi_agent(supervisor: CompiledGraph, initial_message: str):
    for chunk in supervisor.stream(
        {
            "messages": [initial_message],
        },
        stream_mode="values",
        subgraphs=True,
        config={"configurable": {"user_id": "1", "thread_id": "1"}},
    ):
        if len(chunk[0]) > 0:
            state = chunk[1]
            messages = state["messages"]
            last_message = messages[-1]
            last_message.pretty_print()
            print("\n\n")
