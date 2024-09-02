CONDA_ENV_NAME = rag_chatbot_env
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate
CONDA_RUN = conda run -n $(CONDA_ENV_NAME)

.PHONY: all create_env install run test clean format create_sample_data create_faiss_index

all: run

create_or_update_env:
	@echo "Checking if conda environment $(CONDA_ENV_NAME) exists..."
	@if conda env list | grep -q "/$(CONDA_ENV_NAME)"; then \
		echo "Updating existing conda environment $(CONDA_ENV_NAME)..."; \
		CONDA_SUBDIR=osx-arm64 conda env update -f environment.yml; \
	else \
		echo "Creating conda environment $(CONDA_ENV_NAME)..."; \
		CONDA_SUBDIR=osx-arm64 conda env create -f environment.yml; \
	fi

install: create_env
	@echo "Installing additional dependencies..."
	@$(CONDA_RUN) pip install --upgrade pip
	@$(CONDA_RUN) pip install "cmake>=3.21" --upgrade
	@$(CONDA_RUN) pip install faiss-cpu --no-cache-dir
	@$(CONDA_RUN) bash -c 'CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir'

create_sample_data: install
	@echo "Creating sample data..."
	@$(CONDA_RUN) python scripts/create_sample_data.py

create_faiss_index: create_sample_data
	@echo "Creating FAISS index..."
	@$(CONDA_RUN) python scripts/create_faiss_index.py

run: create_faiss_index
	@echo "Running Streamlit app..."
	@$(CONDA_RUN) streamlit run app.py

test: create_env
	@echo "Running tests..."
	@$(CONDA_RUN) PYTHONPATH=$$PYTHONPATH:$$(pwd) pytest tests/

format:
	@echo "Formatting code..."
	@$(CONDA_RUN) black src/ tests/ scripts/ app.py

clean:
	@echo "Removing conda environment..."
	@conda env remove -n $(CONDA_ENV_NAME) -y
