docker stop zad5
docker rm zad5
docker build -t z_5 .
docker run -p 3000:80 --name=zad5 z_5