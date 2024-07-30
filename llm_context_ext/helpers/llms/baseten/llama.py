import requests
import os
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-70B-Instruct")

print("Using Besetens API")

def generate(messages, model_id="7wlxn61w"):
    # baseten_api_key = os.environ["BASETEN_API_KEY"]
    baseten_api_key = "6oXW5sUw.6LHAI5PEtzIvQkFcmDCKYiJcDcr6Afnl"

    data = {
        "prompt": tokenizer.apply_chat_template(messages, tokenize=False),
        "temperature": 0,
        "max_tokens": 8192
    }

    # Call model endpoint
    res = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    return res.text


if __name__ == "__main__":
    res = generate([{"role": "user", "content": "Hello!"}])

    print(res.text)