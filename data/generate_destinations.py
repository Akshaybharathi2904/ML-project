"""
Compiler script to generate all 336 destinations across 28 states and 8 UTs of India.
"""
import json
import shutil
from pathlib import Path

# Load original 15 destinations to preserve their exact IDs and schemas
mock_path = Path("data/mock/destinations.json")
backup_path = Path("data/mock/destinations.backup.json")
if mock_path.exists() and not backup_path.exists():
    shutil.copyfile(mock_path, backup_path)
    print("Backed up original 15 destinations to data/mock/destinations.backup.json")
