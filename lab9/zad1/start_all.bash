# czyszczenie
kubectl scale deployment --all --replicas=0
kubectl delete pods --all
kubectl delete service --all

kubectl apply -f service_b.yaml
kubectl apply -f service_a.yaml


sleep 10
kubectl get services
kubectl get pods
kubectl port-forward service/service-a 5001:80 &