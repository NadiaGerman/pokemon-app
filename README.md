Pokémon App

A modular, Python-based Pokémon application for searching, storing, and managing Pokémon data using the PokéAPI.
Supports multiple database backends: local JSON, MySQL, DynamoDB, and MongoDB.
Easily deployable on AWS and containerized with Docker.

Features

Fetch Pokémon from PokéAPI and save to your chosen backend.
Modular backend: use local JSON, MySQL, DynamoDB, or MongoDB (easy to add more).
Clean, extensible Python code structure.
Environment-configurable (no code changes for backend swap).
Works locally or in the cloud (AWS, Docker, etc).
Folder Structure

pokemon-app/
├── api/               # PokéAPI integration logic
├── battle/            # Battle simulator logic (optional/advanced)
├── constants/         # App-wide constants
├── data/              # Local storage (e.g., pokemon.json)
├── db/                # Modular DB backends (local_db.py, mysql_db.py, dynamodb.py, mongodb.py, __init__.py)
├── scripts/           # Utility scripts (optional)
├── ui/                # User interface/menu logic
├── utils.py           # Shared utilities
├── main.py            # App entry point
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment variables
├── Dockerfile         # Docker support (if using)
└── README.md
└──screenshots         #relevant screenshots
Requirements

Python 3.7+ (recommended: 3.8+)
pip (Python package installer)
If using MySQL, DynamoDB, or MongoDB:
MySQL server or AWS RDS
AWS account & credentials (for DynamoDB)
MongoDB Atlas or local MongoDB (for MongoDB)
Docker (optional)
Setup Instructions

1. Clone the repository
git clone https://github.com/NadiaGerman/pokemon-app.git
cd pokemon-app
2. (Recommended) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
4. Configure Environment Variables
Copy .env.example to .env and edit as needed:

cp .env.example .env
nano .env
Important .env settings:

# Choose your backend: local, mysql, dynamodb, mongodb
DB_BACKEND=local

# For MySQL (if using)
MYSQL_HOST=...
MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_DATABASE=...

# For DynamoDB (if using)
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-west-2
DYNAMO_TABLE=pokemon

# For MongoDB (if using)
MONGO_URI=...
5. (If using MySQL) Install MySQL Connector
pip install mysql-connector-python
6. (If using DynamoDB) Set up AWS credentials
Make sure your user/role has dynamodb:* permissions.

7. Run the App
python3 main.py
Docker (Optional)

Build and run the app in Docker (edit Dockerfile as needed):

docker build -t pokemon-app .
docker run --env-file .env pokemon-app
Switching Database Backends

Just change DB_BACKEND in your .env:

local (default, uses JSON file)
mysql (needs MySQL running and credentials in .env)
dynamodb (needs AWS config)
mongodb (needs MongoDB URI)
No code change required!

Modular DB Design

Each backend is implemented in db/ as its own file (local_db.py, mysql_db.py, etc.).
Switch backends by changing one environment variable.

Terraform & AWS

If using Terraform, refer to the provided PDF for step-by-step AWS provisioning for MySQL and DynamoDB.

Contributing

PRs and issues welcome!

License

MIT (or your preferred license)

Acknowledgements

PokéAPI
AWS Free Tier (for DynamoDB/RDS)
OpenAI/ChatGPT for support and code review
Questions?
Open an issue on GitHub or contact the maintainer.