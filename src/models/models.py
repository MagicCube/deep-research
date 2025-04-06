from langchain_openai import ChatOpenAI


def get_chat_model(model_name="gpt-4o-2024-11-20", **kwargs):
    return ChatOpenAI(model=model_name, temperature=0, max_tokens=4096, **kwargs)
