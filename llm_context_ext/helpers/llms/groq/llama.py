from typing import List

from llm_context_ext.helpers.clients.groq import client

def generate(messages, model="llama-3.1-70b-versatile"):
    return client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=0
    ).choices[0].message.content


if __name__ == "__main__":
    print(generate([
        {"role": "user", "content": "Hello!"}
    ]))