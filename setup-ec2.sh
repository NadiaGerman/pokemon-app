#!/bin/bash

EC2_PUBLIC_IP="44.247.225.39"
SSH_KEY="~/.ssh/myLabKey.pem"
REPO_URL="https://github.com/NadiaGerman/pokemon-app.git"
APP_DIR="pokemon-app"

echo "Connecting to EC2 instance at $EC2_PUBLIC_IP..."

ssh -i $SSH_KEY -t ec2-user@$EC2_PUBLIC_IP << 'ENDSSH'

echo "----------------------------"
echo "🔧 Updating system packages"
echo "----------------------------"
sudo yum update -y
sudo yum install -y git python3

echo "----------------------------"
echo "📁 Cloning GitHub Repository"
echo "----------------------------"
rm -rf pokemon-app
git clone https://github.com/NadiaGerman/pokemon-app.git

echo "----------------------------"
echo "🐍 Setting up Virtual Environment"
echo "----------------------------"
cd pokemon-app
python3 -m venv venv
source venv/bin/activate

echo "----------------------------"
echo "📦 Installing Python Requirements"
echo "----------------------------"
pip install --upgrade pip
pip install -r requirements.txt

# ===============================
# ✅ SHOW MENU
# ===============================
while true; do
  echo ""
  echo "🚀 Pokémon App - What would you like to do?"
  echo "1. Start the App"
  echo "2. Show Files"
  echo "3. Show Python Version"
  echo "4. Exit"
  read -p "Enter choice [1-4]: " choice

  case \$choice in
    1)
      echo "🟢 Starting the Pokémon App..."
      python3 main.py
      ;;
    2)
      echo "📂 Listing files in project directory:"
      ls -l
      ;;
    3)
      echo "🐍 Python version:"
      python3 --version
      ;;
    4)
      echo "👋 Exiting. Goodbye!"
      break
      ;;
    *)
      echo "❌ Invalid choice. Please choose 1-4."
      ;;
  esac
done

ENDSSH
