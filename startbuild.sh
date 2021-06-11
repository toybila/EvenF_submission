#!/bin/bash

docker-compose up -d  --build db  
echo "bulding db container Complete"
echo "Now writing to db"
docker-compose up -d  --build app
echo "bulding app container Complete"
echo "starting training job"
docker-compose up -d  --build trainer
echo "bulding training container Complete"
echo "serving container on 127.0.0.1:5000"