#!/bin/bash
set -e

sudo apt-get update

sudo apt-get install -y git portaudio19-dev python3-scipy python3-aiohttp python3-pip python3-pil python3-numpy python3-gpiozero

if [ ! -d "Canto" ]; then
    git clone https://github.com/Finbear2/Canto.git
fi

cd Canto
git pull

python3 -m pip install sounddevice --break-system-packages
python3 -m pip install spidev --break-system-packages

python3 setup.py

sudo mv canto.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable canto.service
sudo systemctl start canto.service