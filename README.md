This project implements a Retrieval-Augmented Generation (RAG) chatbot using LangChain, FAISS, and Llama-cpp. It's designed to run on macOS with Apple Silicon (M-series) chips.

## Project Structure

```
rag-chatbot/
├── src/
│   ├── __init__.py│ 
│   ├── chatbot.py
│   └── config.py
├── scripts/
│   ├── create_sample_data.py
│   └── create_faiss_index.py
├── configs/
│   └── config.yml
├── app.py
├── Makefile
├── Dockerfile
├── environment.yml
├── requirements.txt
└── README.md
```

## Prerequisites

- macOS with Apple Silicon (M-series) chip
- Miniconda or Anaconda installed
- Xcode Command Line Tools


## Acknowledgments

- LangChain for providing the framework for building the RAG system
- FAISS for efficient similarity search
- Llama-cpp for the language model implementation
- Streamlit for the user interface