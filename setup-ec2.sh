#!/bin/bash

EC2_HOST="44.247.225.39"
PEM_FILE="~/Downloads/myLabKey.pem"
REPO_SSH="git@github.com:NadiaGerman/pokemon-api-app.git" # <- make sure this is correct
APP_DIR="pokemon-api-app"
ENTRY_FILE="main.py"  # Change this if your app runs from another file

echo "Connecting to EC2 instance at $EC2_HOST..."

ssh -o StrictHostKeyChecking=no -i $PEM_FILE ec2-user@$EC2_HOST << EOF

echo "Updating and installing dependencies..."
sudo yum update -y
sudo yum install -y git python3

echo "Cloning your GitHub repo using SSH..."
rm -rf $APP_DIR
git clone $REPO_SSH

echo "Creating and activating virtual environment..."
cd $APP_DIR
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running the Pokémon app in background..."
nohup python3 $ENTRY_FILE > app.log 2>&1 &

echo " App is deployed and running on EC2."
EOF
