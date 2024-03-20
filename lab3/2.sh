docker stop my-server; docker rm my-server; # Opcjonalne czyszczenie
docker run --name my-server -p 80:8080 -d nginx # Mapowanie portów aby aplikacja działała na innym

# sleep 3

docker cp new-conf-file.conf my-server:/etc/nginx/nginx.conf
docker restart my-server;