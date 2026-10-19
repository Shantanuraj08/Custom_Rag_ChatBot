import os
from langchain_community.vectorstores import FAISS

from custom_assistant import config
from custom_assistant.embedding import get_embedding_model


def build_vector_store(chunks):
    """embed every chunks and build
    a searchable vector store"""
    embedding_model=get_embedding_model()
    return FAISS.from_documents(chunks,embedding_model)

def save_vector_store(vector_store,path:str=config.VECTOR_STORE_PATH)->None:
    """"save the faiss index to disk so we don,t have to rebuild it everytime"""
    vector_store.save_local(path)

def load_vector_store(path:str=config.VECTOR_STORE_PATH):
    """"load the vector store to the llm """
    embedding_model=get_embedding_model()
    return FAISS.load_local(path,embedding_model,allow_dangerous_deserialization=True)


def vector_store_exist(path:str=config.VECTOR_STORE_PATH)->bool:
    """check if saved faiss index exist"""
    return os.path.exists(os.path.join(path,"index.faiss"))


def get_retriever(vector_store,k:int=config.TOP_K_RESULT):
    """convert vector_store into retriever that retunr top k chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})