import os
import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict[str, Any]:
    """Load and return the configuration from a JSON file."""
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in config file: {config_path}")
        raise

def ensure_directory_exists(directory: str) -> None:
    """Ensure that the specified directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with values from dict2 overwriting dict1."""
    return {**dict1, **dict2}

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve an environment variable or return a default value."""
    value = os.getenv(key, default)
    if value is None:
        logger.warning(f"Environment variable '{key}' not set, using default: {default}")
    return value

def validate_config(config: Dict[str, Any], required_keys: list) -> bool:
    """Validate that the config contains all required keys."""
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        logger.error(f"Missing required config keys: {missing_keys}")
        return False
    return True