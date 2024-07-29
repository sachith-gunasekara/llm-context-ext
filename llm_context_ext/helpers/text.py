from typing import List

def generate_context_from_message_list(messages: List):
    context = ""
    
    for message in messages:
        context += f"{message['role']}: {message['content']}\n"
    
    return context