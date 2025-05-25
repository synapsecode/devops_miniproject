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


## Adding jenkins

kubectl create namespace jenkins

Created jenkins-deployment.demo

Apply: kubectl apply -f jenkins-deployment.yaml

Access: minikube service jenkins-service -n jenkins

now, to get the secret we must go and get it from
    sudo kubectl get pods -n jenkins
    and we get ID: jenkins-d85d9688-5xpjp

    RUN: kubectl exec -it jenkins-d85d9688-5xpjp -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword

    PASSWORD: ba479e105fe343a08d5630a5439d6d8b

    & Jenkins Authorization is complete!

    Install Plugins
    •	Git
	•	Docker Pipeline
	•	Kubernetes CLI
	•	GitHub Integration



Install docker and kubectl tools also inside the jenkins container
    kubectl exec -it jenkins-d85d9688-5xpjp -n jenkins -- bash

apt-get update && apt-get install -y docker.io curl
curl -LO "https://dl.k8s.io/release/v1.33.1/bin/linux/amd64/kubectl"
chmod +x kubectl && mv kubectl /usr/local/bin/
exit


jenkins dashbaord -> manage jenkins -> credentials -> global -> add new credentials 
    add dockerhub details

