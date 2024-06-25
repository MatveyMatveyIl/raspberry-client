#!/bin/bash

#before start set env
#pipenv shell
cd /home/agroaspect/Documents/projects/raspberry-client
docker-compose -f /home/agroaspect/Documents/projects/raspberry-client/database/docker-compose.yml up -d db
docker-compose -f /home/agroaspect/Documents/projects/raspberry-client-front/docker-compose.yml up -d web
make all
make daemons