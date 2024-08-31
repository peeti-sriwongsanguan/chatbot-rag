CONDA_ENV_NAME = rag_chatbot_env
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate
CONDA_RUN = conda run -n $(CONDA_ENV_NAME)

.PHONY: all create_env install run test clean format create_sample_data create_faiss_index docker-build docker-run

all: run

create_env:
	@echo "Creating conda environment $(CONDA_ENV_NAME)..."
	@conda create -n $(CONDA_ENV_NAME) python=3.9 -y

install: create_env
	@echo "Installing dependencies..."
	@$(CONDA_RUN) pip install -r requirements.txt --upgrade
	@echo "Installing llama-cpp-python for ARM..."
	@$(CONDA_RUN) pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade

create_sample_data: install
	@echo "Creating sample data..."
	@$(CONDA_RUN) python scripts/create_sample_data.py

create_faiss_index: create_sample_data
	@echo "Creating FAISS index..."
	@$(CONDA_RUN) python scripts/create_faiss_index.py

run: create_faiss_index
	@echo "Running Streamlit app..."
	@$(CONDA_RUN) python -m streamlit run app.py

test:
	@echo "Running tests..."
	@$(CONDA_RUN) python -m pytest tests/

format:
	@echo "Formatting code..."
	@$(CONDA_RUN) black src/ tests/ scripts/ app.py

clean:
	@echo "Removing conda environment..."
	@conda env remove -n $(CONDA_ENV_NAME) -y

docker-build:
	@echo "Building Docker image..."
	@docker build -t rag-chatbot .

docker-run:
	@echo "Running Docker container..."
	@docker run -p 8501:8501 rag-chatbot