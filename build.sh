#! /bin/bash

docker build -f ./app/dockerfile.facade ./app -t mak9su4roi/facade
docker build -f ./app/dockerfile.logging ./app -t mak9su4roi/logging
docker build -f ./app/dockerfile.messages ./app -t mak9su4roi/messages

docker push mak9su4roi/facade 
docker push mak9su4roi/logging 
docker push mak9su4roi/messages 