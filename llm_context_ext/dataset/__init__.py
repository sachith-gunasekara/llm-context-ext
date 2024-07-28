from typing import List
import uuid
from dataclasses import dataclass

@dataclass
class DataInstance:
    conversation_id: str = uuid.uuid1().hex
    messages: List
    turns: int

class Dataset:
    data: List[DataInstance] = []

    def add_data(self, messages: List):
        self.data.append(DataInstance(messages=messages, turns=len(messages) / 2))