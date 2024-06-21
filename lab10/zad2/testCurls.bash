curl http://localhost:5000/

curl http://localhost:5000/proxy/jokes

curl http://localhost:5000/proxy/messages

curl -X POST http://localhost:5000/proxy/messages -H "Content-Type: application/json" -d '{"message": "Hello from App A"}'

curl http://localhost:5000/proxy/messages

curl http://localhost:5000/proxy
