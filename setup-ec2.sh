#!/bin/bash

EC2_PUBLIC_IP="44.247.225.39"
KEY_PATH="$HOME/Downloads/myLabKey.pem"

if [ ! -f "$KEY_PATH" ]; then
  echo "❌ SSH key not found at $KEY_PATH"
  exit 1
fi

chmod 400 "$KEY_PATH"

echo "🔌 Connecting to EC2 instance at $EC2_PUBLIC_IP..."

ssh -i "$KEY_PATH" ec2-user@$EC2_PUBLIC_IP << 'ENDSSH'

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

echo "----------------------------"
echo "🎮 Running the Pokémon App Menu"
echo "----------------------------"
chmod +x start-app-menu.sh
./start-app-menu.sh

ENDSSH
