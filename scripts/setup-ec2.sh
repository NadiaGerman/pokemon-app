#!/bin/bash

EC2_PUBLIC_IP="44.247.225.39"
KEY_PATH="$HOME/Downloads/myLabKey.pem"

if [ ! -f "$KEY_PATH" ]; then
  echo " SSH key not found at $KEY_PATH"
  exit 1
fi

chmod 400 "$KEY_PATH"

echo " Connecting to EC2 instance at $EC2_PUBLIC_IP..."
ssh -t -i "$KEY_PATH" ec2-user@$EC2_PUBLIC_IP << 'ENDSSH'

echo "----------------------------"
echo " Running the Pokémon App Menu"
echo "----------------------------"

cd pokemon-app || { echo " Directory pokemon-app not found"; exit 1; }
chmod 777 start-app-menu.sh

#  RUN IT IN A REAL INTERACTIVE SHELL
bash --login -i start-app-menu.sh

ENDSSH
