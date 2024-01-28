#!/bin/bash
echo "Zurg Update Started!"
echo "Stopping dependant containers..."
docker stop plex radarr radarr4k radarr4kdv radarranime sonarr sonarr4k sonarr4kdv sonarranime autoscan prowlarr petio petio-mongo rdtclient

cd /opt/zurg-testing
echo "Zurg is coming down..."
docker compose down

echo "Removing old Zurg images..."
docker image prune -af

echo "Removing old Zurg volumes..."
docker volume prune -af

echo "Composing & updating Zurg..."
docker compose up -d

echo "Waiting for Zurg to initialise..."
sleep 30

docker start plex radarr radarr4k radarr4kdv radarranime sonarr sonarr4k sonarr4kdv sonarranime autoscan prowlarr petio petio-mongo rdtclient
