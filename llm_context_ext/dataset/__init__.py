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

        self.filename = config['data']['Path']

    def _to_json(self):
        keys = DataInstance.get_keys()
        return {key: [getattr(data_instance, key) for data_instance in self] for key in keys}

    def save(self):    
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filepath, "w") as f:
            json.dump(self._to_json(), f)

    def add_data(self, messages: List):
        self.data.append(DataInstance(messages=messages, turns=len(messages) / 2))

        self.save()