import configparser

from pyprojroot import here

config = configparser.ConfigParser()
config.read(here('llm_context_ext/config/config.ini'))