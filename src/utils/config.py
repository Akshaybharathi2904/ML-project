import os
from pathlib import Path
from typing import Any, Dict
import yaml


def get_project_root() -> Path:
    """Return the root path of the project."""
    # This file is in src/utils/config.py -> root is 2 levels up
    return Path(__file__).resolve().parent.parent.parent


def load_config(config_path: str = None) -> Dict[str, Any]:
    """Load configuration YAML file safely."""
    if config_path is None:
        root = get_project_root()
        config_path = str(root / "config.yaml")

    path = Path(config_path)
    if not path.is_absolute():
        path = get_project_root() / path

    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found at: {path}")

    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config

