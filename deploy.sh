#!/bin/sh

docker-compose down

if docker system prune -a; then
        echo "pass"
else
        echo "fail"
fi
git pull

docker-compose build

docker-compose up
