# 🧠 Pokémon API App

This is a command-line Python app that interacts with the [PokéAPI](https://pokeapi.co/). It allows users to fetch random Pokémon, store them locally, and search for saved Pokémon by name.

---

## 📦 Features

- 🎲 Fetch a random Pokémon from PokéAPI
- 💾 Save Pokémon to a local `pokemon.json` file
- 🔍 Search Pokémon by name in the local database
- 📊 View details like name, ID, height, weight, type(s), and stats

---

## 🛠️ Project Structure

pokemon-app/  
│  
├── api.py               # Fetch Pokémon data from API  
├── constants.py         # Stores base API URL  
├── db.py                # Save and read data from local JSON  
├── main.py              # Application entry point with menu  
├── ui.py                # Display and search Pokémon in console  
├── utils.py             # Utility functions (e.g. get random Pokémon)  
├── pokemon.json         # Saved Pokémon data (auto-generated)  
└── README.md            # You're reading it!

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:NadiaGerman/pokemon-app.git
cd pokemon-app

2. Set up the environment
python3 -m venv .venv
source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
3. Run the app
python main.py
🌐 Powered By

PokéAPI
Python 3.10+
requests library

✅ Phase 1: Project Structure and File Reorganization
We’ll create the following structure in your existing pokemon-app/:
pokemon-app/
├── api/              ← Fetch from PokéAPI
│   └── fetcher.py
├── db/               ← DB interfaces: local JSON / DynamoDB
│   ├── local_db.py
│   └── dynamodb.py
├── ui/               ← User interaction
│   └── menu.py
├── core/             ← Business logic
│   └── draw.py
├── constants/        ← Constants and types
│   └── types.py
├── scripts/          ← Automation scripts
│   ├── setup-ec2.sh
│   └── start-app-menu.sh
├── modules/          ← Terraform modules
│   └── dynamodb/
├── .gitignore
├── main.py
├── pokemon.json
├── requirements.txt
├── README.md
└── .env
🔧 Step 1: Create folder structure
Run this from inside your pokemon-app folder:
mkdir -p api db ui core constants scripts modules/dynamodb
mv api.py api/fetcher.py
mv db.py db/local_db.py
mv ui.py ui/menu.py
mv constants.py constants/types.py
mv setup-ec2.sh scripts/
mv start-app-menu.sh scripts/
✅ Step 2: Git commit the structure refactor
After running the above, commit the changes:
git add .
git commit -m "Restructure project into modular folders"
git push origin main
Once done, I’ll begin refactoring the function logic into clean modular Python:
main.py → import clean logic from core/ and ui/
api/fetcher.py → fetch Pokémon from PokéAPI
db/local_db.py → manage JSON storage
db/dynamodb.py → ready for DynamoDB switch
constants/types.py → Pokémon types and logic