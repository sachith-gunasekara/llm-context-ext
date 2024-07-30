import requests
import os

from llm_context_ext.helpers.config import config

print("Using Baseten API")

def generate(messages, model_id=config["baseten"]["ModelID"]):
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    data = messages

    # Call model endpoint
    res = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    return res.content.decode("utf-8")[1:-1].strip()


if __name__ == "__main__":
    res = generate([{"role": "user", "content": "Hello!"}])

    print(res.encode("utf-8", errors="ignore").decode("utf-8"))