#!/bin/bash
# Dubbelklik dit bestand om de site lokaal te bekijken.
cd "$(dirname "$0")" || exit 1
PORT=8000
while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done
echo "Kulé kulé Zanskar — lokale preview op http://localhost:$PORT"
echo "Sluit dit venster om te stoppen."
( sleep 1; open "http://localhost:$PORT" ) &
python3 -m http.server $PORT
