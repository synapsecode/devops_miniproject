# DevOps Project Documentation

## Docker Commands

### Build Docker Image
To build the Docker image for multiple platforms (linux/amd64, linux/arm64):
```sh
docker build --platform linux/amd64,linux/arm64 -t synapsenet/devops-project:latest .
```

### Push Docker Image
To push the Docker image to the repository:
```sh
docker push synapsenet/devops-project:latest
```

## Kubernetes Orchestration

### Apply Deployment and Service
To apply the Kubernetes deployment and service configurations:
```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Check Status
To check the status of the pods and services:
```sh
kubectl get pods
kubectl get svc
```

### Port Forwarding
To forward a local port to a port on the Kubernetes service:
```sh
kubectl port-forward service/devopsproject-service 1111:5000
```
You can then access the service in your browser at: [http://127.0.0.1:1111](http://127.0.0.1:1111)

## Adding Jenkins

### Create Jenkins Namespace
To create a namespace for Jenkins:
```sh
kubectl create namespace jenkins
```

### Deploy Jenkins
To apply the Jenkins deployment configuration:
```sh
kubectl apply -f jenkins-deployment.yaml
```

### Access Jenkins
To access the Jenkins service:
```sh
minikube service jenkins-service -n jenkins
```

### Retrieve Jenkins Admin Password
To retrieve the initial admin password for Jenkins:
1. Get the Jenkins pod ID:
    ```sh
    sudo kubectl get pods -n jenkins
    ```
2. Retrieve the password:
    ```sh
    kubectl exec -it <jenkins-pod-id> -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword
    ```
    Replace `<jenkins-pod-id>` with the actual pod ID.

### Install Jenkins Plugins
Install the following plugins in Jenkins:
- Git
- Docker Pipeline
- Kubernetes CLI
- GitHub Integration

### Install Docker and kubectl in Jenkins Container
To install Docker and kubectl inside the Jenkins container:
```sh
kubectl exec -it <jenkins-pod-id> -n jenkins -- bash
apt-get update && apt-get install -y docker.io curl
curl -LO "https://dl.k8s.io/release/v1.33.1/bin/linux/amd64/kubectl"
chmod +x kubectl && mv kubectl /usr/local/bin/
exit
```
Replace `<jenkins-pod-id>` with the actual pod ID.

### Configure Jenkins Credentials
1. Go to Jenkins Dashboard -> Manage Jenkins -> Credentials -> Global -> Add new credentials.
2. Add Github details.

### Create a New Jenkins Job
1. Create a new Jenkins job.
2. Select Git as the source.
3. Add the repository URL and credentials.
4. Select Git SCM polling.
5. Save the configuration.

### Configure GitHub Webhook
1. Start ngrok to expose Jenkins:
    ```sh
    ngrok http 52938
    ```
2. Go to your GitHub repository -> Settings -> Webhooks -> Add webhook.
3. Set the URL to the ngrok URL followed by `/github-webhook/`.

### Edit Jenkins Project Build Section
Add a build step to execute the following shell script:
```sh
echo "<DOCKERHUB_PASSWORD>" | docker login -u "<DOCKERHUB_USERNAME>" --password-stdin
docker build -t docker.io/synapsenet/devops-project:latest .
docker push docker.io/synapsenet/devops-project:latest
kubectl rollout restart deployment devopsproject -n default
```

### Start Jenkins
To start the Jenkins service:
```sh
sudo minikube service jenkins-service -n jenkins
```

## Regaining Jenkins Access (Reset Password)
To reset the Jenkins admin password:
1. Create a directory for the Groovy script:
    ```sh
    kubectl exec -n jenkins -it <jenkins-pod-id> -- mkdir -p /var/jenkins_home/init.groovy.d
    ```
2. Copy the Groovy script to the Jenkins pod:
    ```sh
    kubectl cp create_admin_user.groovy jenkins/<jenkins-pod-id>:/var/jenkins_home/init.groovy.d/create_admin_user.groovy
    ```
3. Delete the Jenkins pod to apply the changes:
    ```sh
    kubectl delete pod <jenkins-pod-id> -n jenkins
    ```

Replace `<jenkins-pod-id>` with the actual pod ID.

### Jenkins Credentials
- Username: `manas`
- Password: `~1qaz2wsx`

---

This documentation provides a structured and detailed guide for building, deploying, and managing your DevOps project with Docker, Kubernetes, and Jenkins.