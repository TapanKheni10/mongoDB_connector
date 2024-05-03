import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:[%(message)s]')

project_name = "MongoDBConnector"
package_name = "mongodb_connect"

list_of_files = [
    # ".github/workflows/.gitkeep",
    # ".github/workflows/ci.yaml",
    # f"src/{project_name}/__init__.py",
    # f"src/{project_name}/{package_name}/__init__.py",
    # f"src/{project_name}/{package_name}/mongo_crud.py",
    # "config/config.yaml",
    # "params.yaml",
    # "schema.yaml",
    # "main.py",
    # "app.py",
    "research/trails.ipynb",
    # "pages/",
    # "tests/__init__.py",
    # "tests/unit/__init__.py",
    # "tests/unit/unit.py",
    # "tests/integration/__init__.py",
    # "tests/integration/integration.py",
    # "init__setup.sh",
    # "requirements.txt",
    # "requirements_dev.txt",
    # "setup.py",
    # "setup.cfg",
    # "pyproject.toml",
    # "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    ## Getting the directory path and filename
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating an empty file: {filepath}")

    else:
        logging.info(f"{filename} file is already exist. No need to create it.")