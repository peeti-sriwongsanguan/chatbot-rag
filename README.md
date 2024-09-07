# Retrieval-Augmented Generation (RAG) chatbot


This project implements a Retrieval-Augmented Generation (RAG) chatbot using LangChain, FAISS, Llama-cpp, and Streamlit to create a chatbot experience akin to ChatGPT. It's designed to run on macOS with Apple Silicon (M-series) chips.

The RAG ChatBot sifts through the LangChain and then be transformed into vectors using FAISS (Facebook AI Similarity Search) to pick out the most fitting bits. This process looks for the answer in the stored database. These chosen bits help generate accurate answers using a local language model. 

For pretrained model, I used a small hugging-face model called [llama-2-7b.Q4_K_M](https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q4_K_M.gguf) 

![RAG_sample.gif](image%2FRAG_sample.gif)

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
└── README.md
```

## Prerequisites

- macOS with Apple Silicon (M-series) chip
- Miniconda or Anaconda installed
- Xcode Command Line Tools
- Docker (for stability and pushing container images)
- AWS account (for deployment)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/peeti-sriwongsanguan/rag-chatbot.git
   cd rag-chatbot
   ```

2. Create and activate the conda environment:
   ```
   make create_or_update_env
   conda activate rag_chatbot_env
   ```

3. Install dependencies:
   ```
   make install
   ```

## Usage

To run the chatbot locally:

```
make run
```

This command will will create sample data and FAISS index, and start the Streamlit app, therefore, you can interact with the chatbot through your web browser.

## Development

- To run tests:
  ```
  make test
  ```

- To format the code:
  ```
  make format
  ```


## Acknowledgments

- LangChain for providing the framework for building the RAG system
- FAISS for efficient similarity search
- Llama-cpp for the language model implementation
- Streamlit for the user interface