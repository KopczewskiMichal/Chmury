kubectl scale deployment --all --replicas=0
kubectl apply -f my-app-deployment.yaml
sleep 2
kubectl get pods
sleep 2
kubectl get pods
sleep 2
kubectl get pods
sleep 2
kubectl get pods
# kubectl describe pod my-pod
