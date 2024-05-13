docker stop zad4
docker rm zad4
docker build --build-arg PYTHON_VERSION=3.10-alpine -t z_4 .
docker run -p 3000:3000 --name=zad4 z_4