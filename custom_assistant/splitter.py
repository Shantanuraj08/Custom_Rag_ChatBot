from langchain_text_splitters import RecursiveCharacterTextSplitter
from custom_assistant import config

def split_into_chunk(documents):
    """loaded document will be divided into chunks using config values"""
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    return text_splitter.split_documents(documents)