import yaml
from pathlib import Path


def load_config():
    config_path = Path(__file__).parent.parent / 'configs/config.yml'
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Expand user home directory in paths
    if 'llama_model_path' in config:
        config['llama_model_path'] = str(Path(config['llama_model_path']).expanduser())

    if 'faiss_index_path' in config:
        config['faiss_index_path'] = str(Path(config['faiss_index_path']).expanduser())

    return config


# Function to get configuration
def get_config():
    return load_config()

# You can add more configuration functions or classes here if needed