# db/__init__.py


#import os
#from dotenv import load_dotenv; load_dotenv()
#DB_TYPE = os.getenv("DB_TYPE", "local")

#if DB_TYPE == "mongodb":
#    from .mongodb import *
#elif DB_TYPE == "dynamodb":
#    from .dynamodb import *
#else:
#    from .local_db import *

import os
from dotenv import load_dotenv; load_dotenv()
DB_TYPE = os.getenv("DB_TYPE", "local")

if DB_TYPE == "mysql":
    from .mysql_db import insert_pokemon, search_by_name, search_by_id
elif DB_TYPE == "mongodb":
    from .mongodb import insert_pokemon, search_by_name, search_by_id # type: ignore
elif DB_TYPE == "dynamodb":
    from .dynamodb import insert_pokemon, search_by_name, search_by_id
else:
    from .local_db import insert_pokemon, search_by_name, search_by_id

