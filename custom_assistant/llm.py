from langchain_groq import ChatGroq
from custom_assistant import config

def get_llm():
    """return a groq chat model."""
    return ChatGroq(model=config.LLM_MODEL_NAME,temperature=0)