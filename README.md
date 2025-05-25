## Commands

To build:
docker build --platform linux/amd64,linux/arm64 -t synapsenet/devops-project:latest

To push:
docker push synapsenet/devops-project:latest

Kubernetes Orchestration
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check
kubectl get pods
kubectl get svc

Port Forwarding
kubectl port-forward service/devopsproject-service  1111:5000

Check on Browser: http://127.0.0.1:1111

