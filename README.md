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

## Lauch Server
```bash
python3 server.py
```

# Output
Une image **image_result.png** sera crée quand vous ferez "Ctrl+C" pour éteindre le serveur.