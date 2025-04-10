import json
from typing import cast

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_core.messages import AIMessageChunk, HumanMessage, ToolMessage
from langgraph.graph.graph import CompiledGraph
from nanoid import generate as generate_nanoid

from src.agents.researcher import create_agent

app = FastAPI()


def event_stream(graph: CompiledGraph):
    for _, event_type, event_data in graph.stream(
        {"messages": [HumanMessage("安卓最新版本是？")]},
        config={"thread_id": generate_nanoid()},
        stream_mode=["messages"],
        subgraphs=True,
    ):
        message_chunk, message_metadata = cast(
            tuple[AIMessageChunk, dict[str, any]], event_data
        )
        event_stream_message: dict[str, any] = {
            "thread_id": message_metadata["thread_id"],
            "id": message_chunk.id,
            "role": "assistant",
            "content": message_chunk.content,
        }
        if message_chunk.response_metadata.get("finish_reason"):
            event_stream_message["finish_reason"] = message_chunk.response_metadata.get(
                "finish_reason"
            )
        if isinstance(message_chunk, ToolMessage):
            event_stream_message["tool_call_id"] = message_chunk.tool_call_id
            yield f"event: tool_call_result\ndata: {json.dumps(event_stream_message, ensure_ascii=False)}\n\n"
        else:
            yield f"event: message\ndata: {json.dumps(event_stream_message, ensure_ascii=False)}\n\n"


@app.get("/stream")
def stream():
    graph = create_agent()
    return StreamingResponse(event_stream(graph), media_type="text/event-stream")
