# czyszczenie
# kubectl scale deployment --all --replicas=0
# kubectl delete pods --all
# kubectl delete service --all

kubectl apply -f service_a.yaml
kubectl apply -f service_b.yaml


sleep 5
kubectl get services
kubectl get pods
kubectl port-forward service/service-a 5001:80 &
kubectl port-forward service/service-b 5002:5002 &