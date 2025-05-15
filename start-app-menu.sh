#!/bin/bash

echo "----------------------------"
echo "🐍 Activating Virtual Environment"
echo "----------------------------"
cd ~/pokemon-app || exit 1
source venv/bin/activate

# Show Menu
while true; do
  echo ""
  echo "🚀 Pokémon App - What would you like to do?"
  echo "1. Start the App"
  echo "2. Show Files"
  echo "3. Show Python Version"
  echo "4. Exit"
  read -p \"Enter choice [1-4]: \" choice

  case $choice in
    1)
      echo \"🟢 Starting the Pokémon App...\"
      python3 main.py
      ;;
    2)
      echo \"📂 Listing files in project directory:\"
      ls -l
      ;;
    3)
      echo \"🐍 Python version:\"
      python3 --version
      ;;
    4)
      echo \"👋 Exiting. Goodbye!\"
      break
      ;;
    *)
      echo \"❌ Invalid choice. Please choose 1-4.\"
      ;;
  esac
done
