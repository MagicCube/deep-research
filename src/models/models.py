import os

from langchain_openai import ChatOpenAI


def get_chat_model(**kwargs):
    model_name = os.getenv("CHAT_MODEL", "gpt-4o")
    return ChatOpenAI(model=model_name, temperature=0, max_tokens=4096, **kwargs)
