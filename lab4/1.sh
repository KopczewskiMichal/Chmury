# Opcjonalne czyszczenie
docker stop my-server; docker rm my-server;
docker rm my-volume;

docker volume create my-volume

# Używamy tymczasowego kontenera aby móc skopiować pliki do volumenu
docker run -v my-volume:/target --name temp-container busybox true

docker cp ./index.html temp-container:/target/index.html
docker rm temp-container
docker run --name my-server -p 80:80 -d -v my-volume:/usr/share/nginx/html nginx
