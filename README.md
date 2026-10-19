# Custom RAG ChatBot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about an employee policy document. The application loads the policy file, splits it into smaller chunks, creates vector embeddings, and retrieves relevant information to generate grounded answers.

## What this project does

This project provides an **Employee Policy Assistant** that can answer questions such as:

- How many paid annual leave days are available?
- What is the notice period during probation?
- Can employees work from home?
- What are the company holidays?
- What is the reimbursement policy?
- What is the exit process?

The chatbot uses the following RAG workflow:

1. Loads the employee policy from `data/xyz_empolicy.txt`.
2. Splits the document into overlapping text chunks.
3. Generates embeddings using the Jina Embeddings model.
4. Saves or loads a local FAISS vector store from `data/faiss_index`.
5. Retrieves the most relevant policy sections for each question.
6. Uses a Groq language model to generate a clear answer based on the retrieved context.

## Features

- Streamlit chat interface
- Command-line demonstration script
- Local FAISS vector-store caching
- Jina embeddings for semantic search
- Groq LLM integration through LangChain
- Answers grounded in the employee policy document
- Configuration through environment variables

## Project structure

```text
.
├── app.py                         # Streamlit web application
├── main.py                        # Command-line demonstration
├── requirements.txt               # Python dependencies
├── data/
│   ├── xyz_empolicy.txt           # Source employee policy document
│   └── faiss_index/               # Generated local vector store
└── custom_assistant/
    ├── agent.py                   # LangChain agent creation
    ├── config.py                  # Environment variables and settings
    ├── document_loader.py         # Policy document loader
    ├── embedding.py               # Jina embedding model
    ├── llm.py                     # Groq language model
    ├── pipeline.py                # End-to-end RAG pipeline
    ├── splitter.py                # Document chunking
    ├── tools.py                   # Policy search tool
    └── vector_store.py             # FAISS vector-store operations
```

## Requirements

- Python 3.9 or newer
- A Groq API key
- A Jina AI API key
- Internet access for the LLM and embedding APIs

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shantanuraj08/Custom_Rag_ChatBot.git
cd Custom_Rag_ChatBot
```

### 2. Create and activate a virtual environment

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment variables

Create a file named `.env` in the project root:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
```

Do not commit `.env` or expose your API keys publicly.

## Run the Streamlit web app

The recommended way to use the chatbot is through the Streamlit interface:

```bash
streamlit run app.py
```

After starting, Streamlit will display a local URL, normally:

```text
http://localhost:8501
```

Open that URL in your browser and ask questions about the employee policy.

The FAISS index is created automatically the first time the application starts. Later runs reuse the saved index from `data/faiss_index`.

## Run the command-line demo

To run the predefined example questions from `main.py`:

```bash
python main.py
```

This script demonstrates questions about annual leave, probation notice periods, and working from home.

## Using your own policy document

1. Replace `data/xyz_empolicy.txt` with your own plain-text policy document.
2. Remove the existing vector store so it can be rebuilt:

```bash
rm -rf data/faiss_index
```

On Windows PowerShell:

```powershell
Remove-Item -Recurse -Force data/faiss_index
```

3. Start the application again:

```bash
streamlit run app.py
```

The application will create a new FAISS index from the updated document.

## Configuration

The main configuration values are defined in `custom_assistant/config.py`:

- `LLM_MODEL_NAME`: Groq model used to generate answers
- `EMBEDDING_MODEL_NAME`: Jina embedding model used for retrieval
- `CHUNK_SIZE`: Maximum size of each document chunk
- `CHUNK_OVERLAP`: Number of overlapping characters between chunks
- `TOP_K_RESULT`: Number of relevant chunks retrieved for each question
- `DATH_FILE_PATH`: Path to the source policy document
- `VECTOR_STORE_PATH`: Path to the local FAISS index

## Troubleshooting

### Missing API key error

Make sure `.env` exists in the project root and contains both required keys:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
```

### FAISS index or old answers

Delete the cached vector store and restart the application:

```bash
rm -rf data/faiss_index
streamlit run app.py
```

### `streamlit` command not found

Activate the virtual environment and reinstall the dependencies:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Technologies used

- Python
- Streamlit
- LangChain
- LangChain Groq
- Jina Embeddings
- FAISS
- python-dotenv

## Tip and current limitation

**Tip:** Upload or replace the policy file with a document specific to your needs to turn this project into a personalized chatbot. For example, you can use a company handbook, product guide, course material, or any other relevant text document and then rebuild the FAISS index.

**Current limitation:** The application currently supports only **one file at a time**. To use a different file, replace the existing document and rebuild the vector store before restarting the application.
