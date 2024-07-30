from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-70B-Instruct")

messages = [
    {
        "role": "system",
        "content": "You are a pirate."
    },
    {
        "role": "user",
        "content": "Tell me a story."
    },
    {
        "role": "assistant",
        "content": "Yay Yay Yay"
    }

]

print(tokenizer.apply_chat_template(messages, tokenize=False))