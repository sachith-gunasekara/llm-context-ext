from groq import Groq
from dotenv import load_dotenv
import os

def create_groq_client(groq_api_key: str):
    return Groq(api_key=groq_api_key)

client = create_groq_client(os.environ["GROQ_API_KEY"])