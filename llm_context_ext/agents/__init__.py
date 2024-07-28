from abc import ABC, abstractmethod
from typing import List


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
    def generate(self, user_message: str):
        pass