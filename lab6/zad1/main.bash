docker network create --subnet 192.168.1.0/24 --gateway 192.168.1.1 --driver bridge my_bridge
docker run -d --name my_container --network my_bridge alpine sh -c "while true; do echo 'Running...'; sleep 60; done"
sleep 3
docker exec -it my_container sh -c "ping -c 4 192.168.1.1"
docker network inspect my_bridge
