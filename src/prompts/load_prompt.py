import os
from datetime import datetime
from typing import Literal

prompt_cache = {}


def load_prompt(
    prompt_name: Literal["coder", "planner", "researcher", "supervisor"],
) -> str:
    if prompt_name in prompt_cache:
        return prompt_cache[prompt_name]
    file_name = os.path.join(os.path.dirname(__file__), f"{prompt_name}.md")
    with open(file_name, "r") as f:
        prompt = (
            f"---\ncurrent_time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n---\n\n"
            + f.read()
        )
        prompt_cache[prompt_name] = prompt
        return prompt
