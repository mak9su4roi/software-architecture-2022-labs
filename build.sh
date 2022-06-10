#! /bin/bash

docker build -f ./app/dockerfile.facade ./app -t mbilyk/facade:v4
docker build -f ./app/dockerfile.logging ./app -t mbilyk/logging:v4
docker build -f ./app/dockerfile.messages ./app -t mbilyk/messages:v4

docker push mbilyk/facade:v4
docker push mbilyk/logging:v4
docker push mbilyk/messages:v4