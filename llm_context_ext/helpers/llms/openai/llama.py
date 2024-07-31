from llm_context_ext.helpers.config import config
from llm_context_ext.helpers.clients.openai import client


print("Using NVIDIA API")

def generate(messages, model=config["model"]["Name"]):
    return client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=0
    ).choices[0].message.content


if __name__ == "__main__":
    print(generate([
        {"role": "user", "content": "Hello!"}
    ]))