import os
import random

from datasets import load_dataset
from dotenv import load_dotenv

load_dotenv()

from llm_context_ext.dataset import Dataset
from llm_context_ext.agents.assistant import Assistant
from llm_context_ext.agents.critic import Critic
from llm_context_ext.agents.user import User
from llm_context_ext.helpers.text import generate_context_from_message_list
from llm_context_ext.helpers.re import extract_task_from_content, extract_hints_from_content, extract_follow_up_message_from_content
from llm_context_ext.helpers.config import config
from llm_context_ext.init.logger import logger


MIN_N_TURNS = config.getint('run', 'MinNTurns')
MAX_N_TURNS = config.getint('run', 'MaxNTurns')
SEED_DATASET = config["dataset"]["SeedDataset"]
SEED_DATASET_SUBSET = config["dataset"]["SeedDatasetSubset"]
SEED_COUNT = config.getint("dataset", "SeedCount")


# Load Cosmopedia openstax subset
cosmopedia_ds = load_dataset(SEED_DATASET, SEED_DATASET_SUBSET, split="train")

# Initialize our dataset
dataset = Dataset()

# Select 25000 - already available instances in our dataset
cosmopedia_ds = cosmopedia_ds.shuffle(seed=42).select(range(len(dataset), SEED_COUNT))
logger.info(f"Selected {len(cosmopedia_ds)} examples from the seed dataset")

def run_chat_turn(assistant: Assistant, user_message: str, turn_idx: int, n_turns: int):
    assistant_response = assistant.chat(user_message)

    if (turn_idx + 1) != n_turns:
        user = User()
        critic = Critic()

        first_user_message = assistant.messages[1]["content"]
        context_for_critic = generate_context_from_message_list(assistant.messages[2:])

        critic_response = critic.chat(first_user_message, context_for_critic)
    
        task, hints = extract_task_from_content(critic_response), extract_hints_from_content(critic_response)

        context_for_user = generate_context_from_message_list(assistant.messages[1:])
        user_response = user.chat(task, hints, context_for_user)

        follow_up_message = extract_follow_up_message_from_content(user_response)

        return follow_up_message
    
    return None
    

for example in cosmopedia_ds:
    try:
        n_turns = random.randint(MIN_N_TURNS, MAX_N_TURNS)
    
        logger.info(f"Starting chat with {n_turns} turns")
        user_message = example["prompt"]
    
        logger.info("Checking if example has already been seen")
        if user_message in dataset:
            logger.warning("Skipping example because it has already been seen")
            continue
    
        logger.info("Running chat")
        assistant = Assistant()
        for turn_idx in range(n_turns):
            user_message = run_chat_turn(assistant, user_message, turn_idx, n_turns)
    
        logger.info("Adding conversatiion instance to the dataset")
        dataset.add_data(assistant.messages[1:])
    except Exception as e:
        logger.error("Exception occured\n: %s", e)
    finally:
        continue