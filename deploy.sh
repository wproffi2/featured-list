#!/bin/sh

docker-compose down

docker system prune -a

git pull

docker-compose build

docker-compose up -d 
