import random

from datasets import load_dataset

from llm_context_ext.dataset import Dataset
from llm_context_ext.agents.assistant import Assistant
from llm_context_ext.agents.critic import Critic
from llm_context_ext.agents.user import User


MIN_N_TURNS = 1
MAX_N_TURNS = 5


# Load Cosmopedia openstax subset
cosmopedia_ds = load_dataset("HuggingFaceTB/cosmopedia", "openstax", split="train").shuffle().select(range(25000))

# Initialize our dataset
dataset = Dataset()

def run_chat_turn(assistant: Assistant, user_message: str, turn_idx: int, n_turns: int):
    user = User()
    critic = Critic()

    assistant_response = assistant.generate(user_message)

    if (turn_idx + 1) != n_turns:
        first_user_message = assistant.messages[1].content
        context = ""
        for message in assistant.messages[2:]:
            context += f"{message['role']}: {message['content']}\n"

        critic_response = critic.generate(first_user_message, context)
    
    

for example in cosmopedia_ds:
    n_turns = random.randint(MIN_N_TURNS, MAX_N_TURNS)

    