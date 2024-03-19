#!/bin/bash

docker build -t nodejs_server .

docker run -p 8080:8080 -d --name node_server nodejs_server 
docker exec node_server node index.js