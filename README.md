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
    kubectl exec -it jenkins-d85d9688-c9sz6 -n jenkins -- bash

apt-get update && apt-get install -y docker.io curl
curl -LO "https://dl.k8s.io/release/v1.33.1/bin/linux/amd64/kubectl"
chmod +x kubectl && mv kubectl /usr/local/bin/
exit


jenkins dashbaord -> manage jenkins -> credentials -> global -> add new credentials 
    add dockerhub details

Create a new Config
    Select Git
    Add Reposotory URL and credentials
    select Git SCM polling
    Save


ngrok http 52938

Go to GithubRepo > settings > WebHook > add
    URL:  https://45e2-2405-201-d036-2841-dc98-815-b7a6-7292.ngrok-free.app/github-webhook/



Edit Project Build Section on Jenkins

- Add Build Step > Execute Shell
```
#!/bin/bash

echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
docker build -t docker.io/synapsenet/devops-project:latest .
docker push docker.io/synapsenet/devops-project:latest
kubectl rollout restart deployment devopsproject -n default
```

Add DOCKER_USER, DOCKER_PASS bindings to Configure > Environemnt


jenkins start: sudo  minikube service jenkins-service -n jenkins


### Regaining Jenkins Access (Wipe-password)
kubectl exec -n jenkins -it jenkins-d85d9688-5xpjp -- mkdir -p /var/jenkins_home/init.groovy.d
kubectl cp create_admin_user.groovy jenkins/jenkins-d85d9688-5xpjp:/var/jenkins_home/init.groovy.d/create_admin_user.groovy
kubectl delete pod jenkins-d85d9688-5xpjp -n jenkins

### Jenkins Details
manas
~1qaz2wsx