from langchain_community.embeddings import JinaEmbeddings
from custom_assistant import config

def get_embedding_model():
    """embedding model is fetched"""
    return JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)