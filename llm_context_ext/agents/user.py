from llm_context_ext.agents import LLMAgent
from llm_context_ext.helpers.file import read_system_message, read_user_message
from llm_context_ext.helpers.llms.llama import generate as llama_generate


class User(LLMAgent):
    user_message_template: str

    def __init__(self):
        super().__init__(read_system_message(self))
        self.user_message_template = read_user_message(self)
    
    def generate(self, task: str, hints: str, context: str):
        user_message = self.user_message_template.format(task=task, hints=hints, context=context)

        self.messages.append(
            {
                "role": "user", 
                "content": user_message
            }
        )

        response = llama_generate(self.messages)

        return response