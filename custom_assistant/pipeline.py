from custom_assistant import config
from custom_assistant.agent import create_custom_agent
from custom_assistant.llm import get_llm
from custom_assistant.tools import create_search_tool
from custom_assistant.document_loader import load_document
from custom_assistant.splitter import split_into_chunk
from custom_assistant.vector_store import (
  build_vector_store,
  load_vector_store,
  save_vector_store,
  get_retriever,
  vector_store_exist,  
)


def build_vector_store_from_documents(file_path:str=config.DATH_FILE_PATH):
    if vector_store_exist():
        print("found vector store on disk ,loading it")
        return load_vector_store()

    print("no vector store found,building it")
    documents=load_document(file_path)
    chunks=split_into_chunk(documents)
    print(f"loaded`{file_path}`and split into {len(chunks)}chunks")

    vector_store=build_vector_store(chunks)
    save_vector_store(vector_store)
    return vector_store

def build_custom_agent(file_path:str=config.DATH_FILE_PATH):
    """build rag agent to answer your query"""
    config.check_api_key()
    vector_store=build_vector_store_from_documents(file_path)
    retriever=get_retriever(vector_store)
    search_tool=create_search_tool(retriever)

    llm=get_llm()
    agent=create_custom_agent(llm,[search_tool])

    return agent


def ask(agent,question:str)->str:
    """ask agent question and it will answer it"""
    response=agent.invoke({"messages":[{"role":"user","content":question}]})
    return response["messages"][-1].content
        