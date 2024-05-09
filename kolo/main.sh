docker stop my-server
docker rm my-server

docker build -t my-server .
sleep 3
docker run -d -p 8080:8080 -d --name my-server my-server
docker exec my-server node server.js
