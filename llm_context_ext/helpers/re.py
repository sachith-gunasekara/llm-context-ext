import re

from llm_context_ext.helpers.config import config

def extract_text_between_tags(text: str, start_tag: str, end_tag: str) -> str:
    # Regular expression to match the content between the start and end tags
    pattern = f"{re.escape(start_tag)}(.*?){re.escape(end_tag)}"

    # Find the first match in the text
    match = re.search(pattern, text, re.DOTALL)

    if match:
        # Extract the content between the start and end tags
        content = match.group(1)
        return content.strip()
    else:
        # If end tag is missing, extract content after start tag
        start_index = text.find(start_tag)
        
        if start_index != -1:
            return text[start_index + len(start_tag):]
        
        return ""

def extract_task_from_content(content: str) -> str:
    TASK_START_TAG = config["patterns"]["TaskStartTag"]
    TASK_END_TAG = config["patterns"]["TaskEndTag"]

    return extract_text_between_tags(content, TASK_START_TAG, TASK_END_TAG)

def extract_hints_from_content(content: str) -> str:
    HINTS_START_TAG = config["patterns"]["HintsStartTag"]
    HINTS_END_TAG = config["patterns"]["HintsEndTag"]

    return extract_text_between_tags(content, HINTS_START_TAG, HINTS_END_TAG)

def extract_follow_up_message_from_content(content: str) -> str:
    FOLLOW_START_TAG = config["patterns"]["FollowStartTag"]
    FOLLOW_END_TAG = config["patterns"]["FollowEndTag"]

    return extract_text_between_tags(content, FOLLOW_START_TAG, FOLLOW_END_TAG)