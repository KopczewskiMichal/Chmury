./stop_production.bash
./build.bash
kubectl apply -f main.yaml
sleep 10
kubectl port-forward deployment.apps/app-a-deployment 5000:5000 &
kubectl port-forward service/service-b 3000:3000 &
kubectl get all