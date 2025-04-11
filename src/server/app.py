import json
from typing import cast

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_core.messages import AIMessageChunk, HumanMessage, ToolMessage
from langgraph.graph.graph import CompiledGraph
from nanoid import generate as generate_nanoid

from src.agents.supervisor import create_agent

app = FastAPI()


@app.get("/stream")
def stream():
    graph = create_agent()
    return StreamingResponse(_event_stream(graph), media_type="text/event-stream")


def _make_event(event_type: str, data: dict[str, any]):
    if data.get("content") == "":
        data.pop("content")
    return f"event: {event_type}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def _event_stream(graph: CompiledGraph):
    for _, _, event_data in graph.stream(
        {"messages": [HumanMessage("南京小笼包和上海小笼包有什么区别？")]},
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
            # Tool Message - Return the result of the tool call
            event_stream_message["tool_call_id"] = message_chunk.tool_call_id
            yield _make_event("tool_call_result", event_stream_message)
        else:
            # AI Message - Raw message tokens
            if message_chunk.tool_calls:
                # AI Message - Tool Call
                event_stream_message["tool_calls"] = message_chunk.tool_calls
                yield _make_event("tool_call", event_stream_message)
            if message_chunk.tool_call_chunks:
                # AI Message - Tool Call Chunks
                event_stream_message["tool_call_chunks"] = (
                    message_chunk.tool_call_chunks
                )
                yield _make_event("tool_call_chunk", event_stream_message)
            else:
                # AI Message - Raw message tokens
                yield _make_event("message_chunk", event_stream_message)
