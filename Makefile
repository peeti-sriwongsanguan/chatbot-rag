CONDA_ENV_NAME = rag_chatbot_env
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

.PHONY: all create_env install run test clean format

all: create_env install

create_env:
	conda create -n $(CONDA_ENV_NAME) python=3.9 -y

install: create_env
	$(CONDA_ACTIVATE) $(CONDA_ENV_NAME) && \
	pip install streamlit langchain faiss-cpu sentence-transformers pytest black python-dotenv llama-cpp-python

run:
	$(CONDA_ACTIVATE) $(CONDA_ENV_NAME) && \
	python -m streamlit run chatbot.py

test:
	$(CONDA_ACTIVATE) $(CONDA_ENV_NAME) && \
	pytest test_chatbot.py

format:
	$(CONDA_ACTIVATE) $(CONDA_ENV_NAME) && \
	black .

clean:
	conda env remove -n $(CONDA_ENV_NAME) -y