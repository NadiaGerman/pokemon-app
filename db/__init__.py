# db/__init__.py

import os
from dotenv import load_dotenv
load_dotenv()

# Use a single environment variable to select DB backend
DB_BACKEND = os.getenv("DB_BACKEND", "local").lower()

if DB_BACKEND == "mysql":
    from .mysql_db import insert_pokemon, search_by_name, search_by_id
elif DB_BACKEND == "dynamodb":
    from .dynamodb import insert_pokemon, search_by_name, search_by_id
elif DB_BACKEND == "mongodb":
    from .mongodb import insert_pokemon, search_by_name, search_by_id  # type: ignore
elif DB_BACKEND == "local":
    from .local_db import insert_pokemon, search_by_name, search_by_id
else:
    raise ValueError(f"Unsupported DB_BACKEND: {DB_BACKEND}")

DB_BACKEND = os.getenv("DB_BACKEND") or os.getenv("DB_TYPE", "local").lower()
if DB_BACKEND not in ["mysql", "dynamodb", "mongodb", "local"]:
    raise ValueError(f"Unsupported DB_BACKEND: {DB_BACKEND}")