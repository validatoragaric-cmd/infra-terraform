import os
import logging

def get_project_root() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def get_config_file_path(file_name: str) -> str:
    project_root = get_project_root()
    return os.path.join(project_root, 'config', file_name)

def setup_logging(log_level: int = logging.INFO) -> None:
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        level=log_level
    )

def load_config(file_name: str) -> dict:
    import json
    file_path = get_config_file_path(file_name)
    with open(file_path, 'r') as file:
        return json.load(file)

def write_config(file_name: str, config: dict) -> None:
    import json
    file_path = get_config_file_path(file_name)
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)