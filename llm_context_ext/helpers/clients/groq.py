import os

from groq import Groq


client = Groq(api_key=os.environ["GROQ_API_KEY"])