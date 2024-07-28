from llm_context_ext.agents import LLMAgent

from llm_context_ext.helpers.file import read_system_message, read_user_message
from llm_context_ext.helpers.llms.llama import generate as llama_generate

class Assistant(LLMAgent):

    def __init__(self):
        super().__init__(read_system_message(self))
    
    def generate(self, user_message: str):
        self.messages.append(
            {
                "role": "user", 
                "content": user_message
            }
        )

        response = llama_generate(self.messages)

        self.messages.append(
            {
                "role": "assistant", 
                "content": response
            }
        )

        return response
        


if __name__ == "__main__":
    assistant = Assistant()

    print(assistant.system_message)
    print("==========================================")
    print(assistant.user_message)