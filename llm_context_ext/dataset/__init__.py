import os
import json
import uuid
from typing import List, Set, Union
from dataclasses import dataclass

from pyprojroot import here

from llm_context_ext.helpers.config import config

@dataclass
class DataInstance:
    messages: List
    turns: int
    model: str = config["model"]["Name"]
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
        self.filename = os.path.join(config['data']['Path'], "data.json")

        if os.path.exists(self.filename):
            self.load()
    
    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

    def __contains__(self, first_user_message: str):
        return any(data_instance.messages[0]["content"].strip().lower() == first_user_message.strip().lower() for data_instance in self)

    def _to_json(self):
        keys = DataInstance.get_keys()
        return {key: [getattr(data_instance, key) for data_instance in self] for key in keys}

    def _from_json(self):
        keys = DataInstance.get_keys()

        with open(self.filename, "r") as f:
            data = json.load(f)

        return [DataInstance(**instance) for instance in [{key: data[key][i] for key in keys} for i in range(len(data[keys[0]]))]]

    def load(self):
        self.data = self._from_json()

    def save(self):    
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        with open(self.filename, "w") as f:
            json.dump(self._to_json(), f)

    def add_data(self, messages: List):
        self.data.append(DataInstance(messages=messages, turns=int(len(messages) / 2)))

        self.save()
    
    def remove_data(self, idxs: Union[List, Set]):
        self.data = [ele for idx, ele in enumerate(self.data) if idx not in idxs]
    
    def to_hf_dataset(self):
        from datasets import Dataset as HF_Dataset
        
        return HF_Dataset.from_dict(self._to_json())