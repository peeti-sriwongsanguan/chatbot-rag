import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import yaml

def create_faiss_index():
    # Load configuration
    with open('configs/config.yml', 'r') as f:
        config = yaml.safe_load(f)

    # Read the raw data
    with open('data/raw/climate_change.txt', 'r') as f:
        raw_text = f.read()

    # Split the text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(raw_text)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=config['embeddings_model'])

    # Create and save FAISS index
    try:
        db = FAISS.from_texts(texts, embeddings)
        db.save_local(config['faiss_index_path'])
        print(f"FAISS index created and saved to {config['faiss_index_path']}")
    except ImportError as e:
        print(f"Error: {e}")
        print("Please ensure faiss-cpu is installed correctly.")
        print("You can try: pip install faiss-cpu --no-cache-dir")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_faiss_index()