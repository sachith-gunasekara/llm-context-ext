from abc import ABC, abstractmethod
from typing import List

# from llm_context_ext.helpers.llms.groq.llama import generate as groq_llama_generate
# from llm_context_ext.helpers.llms.baseten.llama import generate as baseten_llama_generate
from llm_context_ext.helpers.llms.baseten.mistral import generate as baseten_mistral_generate


generate = baseten_mistral_generate

class LLMAgent(ABC):
    system_message: str
    messages: List

    def __init__(self, system_message: str):
        self.system_message = system_message
        self.messages = [
            {
                "role": "system", 
                "content": self.system_message
            }
        ]

    @abstractmethod
    def chat(self):
        pass

    def generate(self):
        return generate(self.messages)