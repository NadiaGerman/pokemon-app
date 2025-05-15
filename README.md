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