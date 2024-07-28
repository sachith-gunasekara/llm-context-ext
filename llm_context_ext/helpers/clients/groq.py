import os

from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def create_groq_client():
    return Groq(api_key=GROQ_API_KEY)

client = create_groq_client()