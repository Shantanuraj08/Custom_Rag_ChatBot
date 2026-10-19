from langchain_community.document_loaders import TextLoader
from custom_assistant import config

def load_document(file_path:str=config.DATH_FILE_PATH):
    """load documents to be chunked"""
    loader=TextLoader(file_path,encoding="utf-8")
    return loader.load()