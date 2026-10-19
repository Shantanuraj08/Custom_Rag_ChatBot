from langchain.agents import create_agent
from custom_assistant import config

def create_custom_agent(llm,tools):
    """create a emp policy answering agent .which give answer to question of employee"""
    return create_agent(model=llm,tools=tools,system_prompt=config.SYSTEM_PROMPT)