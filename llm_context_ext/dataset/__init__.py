import os
import json
import uuid
import configparser
from typing import List
from dataclasses import dataclass

from pyprojroot import here

@dataclass
class DataInstance:
    messages: List
    turns: int
    conversation_id: str = uuid.uuid1().hex

    @staticmethod
    def get_keys():
        inst = DataInstance([], 1)
        
        attributes = [attr for attr in dir(inst) if not callable(getattr(inst, attr)) and not attr.startswith("__")]
        return attributes

class Dataset:
    data: List[DataInstance] = []
    filename: str

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(here('llm_context_ext/config/config.ini'))

        self.filename = os.path.join(config['data']['Path'], "data.json")

        if os.path.exists(self.filename):
            self.data = self._from_json()
    
    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

    def _to_json(self):
        keys = DataInstance.get_keys()
        return {key: [getattr(data_instance, key) for data_instance in self] for key in keys}

    def _from_json(self):
        keys = DataInstance.get_keys()

        with open(self.filename, "r") as f:
            data = json.load(f)

        return [DataInstance(**instance) for instance in [{key: data[key][i] for key in keys} for i in range(len(data[keys[0]]))]]

    def save(self):    
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        with open(self.filename, "w") as f:
            json.dump(self._to_json(), f)

    def add_data(self, messages: List):
        self.data.append(DataInstance(messages=messages, turns=int(len(messages) / 2)))

        self.save()