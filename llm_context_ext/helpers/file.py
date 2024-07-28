import configparser

from pyprojroot import here

config = configparser.ConfigParser()
config.read(here("llm_context_ext/config/config.ini"))


def read_txt(file_path: str):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def read_system_message(agent_class):
    file_path = f"{config['prompts']['Path']}/{agent_class.__class__.__name__.lower()}/system_message.txt"
    return read_txt(file_path)

def read_user_message(agent_class):
    file_path = f"{config['prompts']['Path']}/{agent_class.__class__.__name__.lower()}/user_message.txt"
    return read_txt(file_path)