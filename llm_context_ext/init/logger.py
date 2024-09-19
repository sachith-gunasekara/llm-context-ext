import logging

from pyprojroot import here

logger = logging.getLogger("llm-context-ext")

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(here("llm_context_ext/logs/log.txt"))

c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.setLevel(logging.DEBUG)

logger.info('Logger initialized')