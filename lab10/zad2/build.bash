docker build -t mkopczewski/app-a-image ./app_a/
docker push mkopczewski/app-a-image

docker build -t mkopczewski/app-b-image ./app_b/
docker push mkopczewski/app-b-image