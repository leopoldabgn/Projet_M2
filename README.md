# Projet M2 - Side Channel Attack

# Client

## Chrome Version 83

### Installation Link
https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/756066/

### Launch command
```bash
unzip Linux...chrome.zip
cd chrome-linux/
./chrome --disable-gpu --disable-software-rasterizer --no-sandbox ../code/client/exploit.html
```

# Server

## Install Python Packages
```bash
cd code/server
pip install -r requirements.txt
```

## Launch Server
Se lance sur le port 7000 en localhost.
```bash
python3 server.py
```

# Output
Une image **output/img1.png** sera crée quand vous ferez "Ctrl+C" pour éteindre le serveur.

# NOTES

## Ouvrir un port uniquement visible sur la machine
python3 -m http.server 5000 --bind 127.0.0.1
