#!/bin/bash

EC2_PUBLIC_IP="44.247.225.39"
KEY_PATH="$HOME/Downloads/myLabKey.pem"

if [ ! -f "$KEY_PATH" ]; then
  echo " SSH key not found at $KEY_PATH"
  exit 1
fi

chmod 400 "$KEY_PATH"

echo " Connecting to EC2 instance at $EC2_PUBLIC_IP..."
ssh -i "$KEY_PATH" ec2-user@$EC2_PUBLIC_IP
ssh -i "$KEY_PATH" ec2-user@$EC2_PUBLIC_IP << 'ENDSSH'

echo "----------------------------"
echo "📦 Running the Pokémon App Menu"
echo "----------------------------"

cd pokemon-app
chmod +x start-app-menu.sh
./start-app-menu.sh

ENDSSH


