#!/bin/bash

docker stop plex radarr radarr4k radarr4kdv radarranime sonarr sonarr4k sonarr4kdv sonarranime autoscan prowlarr petio petio-mongo rdtclient

cd /opt/zurg-testing

docker compose down

docker image prune -f

docker volume prune -f

docker compose up -d

echo "Waiting for 60 seconds..."
sleep 60

docker start plex radarr radarr4k radarr4kdv radarranime sonarr sonarr4k sonarr4kdv sonarranime autoscan prowlarr petio petio-mongo rdtclient
