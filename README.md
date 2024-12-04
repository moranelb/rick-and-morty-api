# Rick and Morty REST API Kubernetes Deployment with Helm and CI/CD

This project deploys a Flask-based REST API application to a Kubernetes cluster using Helm and integrates with GitHub Actions for automated deployment and testing.

## Features
- Fetch characters from the Rick and Morty API with filters (species, status, origin).
- Kubernetes deployment using Helm charts.
- CI/CD workflow using GitHub Actions.

---

## Prerequisites
- Docker installed and set up.
- Minikube installed and running.
- Kubernetes CLI (`kubectl`) installed.
- Helm installed.
- GitHub repository with this codebase.

---

## Steps to Deploy

### 1. Kubernetes Deployment
#### Using Kubernetes Manifests
1. **Navigate to the `yamls` directory**:
   ```bash
   cd yamls
   ```

2. **Apply the Kubernetes manifests**:
   ```bash
   kubectl apply -f Deployment.yaml
   kubectl apply -f Service.yaml
   kubectl apply -f Ingress.yaml
   ```

3. **Verify the deployment**:
   ```bash
   kubectl get pods
   kubectl get services
   kubectl get ingress
   ```

4. **Access the application**:
   - Edit your local `/etc/hosts` file and add the following entry:
     ```
     127.0.0.1 rick-and-morty.local
     ```
   - If running Minikube on Docker, ensure you run:
     ```bash
     minikube tunnel
     ```
   - Access the application at [http://rick-and-morty.local](http://rick-and-morty.local).

---

### 2. Deploy Using Helm
1. **Navigate to the `helm` directory**:
   ```bash
   cd helm/rick-and-morty-api
   ```

2. **Install the Helm chart**:
   ```bash
   helm install rick-and-morty-api .
   ```

3. **Verify the Helm release**:
   ```bash
   helm list
   ```

4. **Access the application**:
   - Same as in the Kubernetes deployment step.

---

### 3. GitHub Actions Workflow
#### Overview
The workflow automates the following tasks:
- Sets up a Kubernetes cluster on the GitHub Actions runner.
- Deploys the application using Helm.
- Tests the application endpoints.

#### Workflow File
The workflow file is located at `.github/workflows/deploy-test.yaml`. The workflow includes the following jobs:
1. **Cluster Setup**:
   - Uses `kind` to create a local Kubernetes cluster on the GitHub Actions runner.
2. **Application Deployment**:
   - Installs Helm.
   - Deploys the application to the cluster using the Helm chart.
3. **Endpoint Testing**:
   - Runs tests on the `/healthcheck` and `/fetch_characters` endpoints.

#### Running the Workflow
1. Push changes to your repository to trigger the workflow:
   ```bash
   git push origin main
   ```

2. Monitor the workflow execution in the "Actions" tab of your GitHub repository.

---

### Endpoints
1. **Health Check**:
   - Endpoint: `/healthcheck`
   - Example: [http://rick-and-morty.local/healthcheck](http://rick-and-morty.local/healthcheck)

2. **Fetch Characters**:
   - Endpoint: `/fetch_characters`
   - Example: [http://rick-and-morty.local/fetch_characters?species=Human&status=Alive&origin=Earth](http://rick-and-morty.local/fetch_characters?species=Human&status=Alive&origin=Earth)

---

### Directory Structure
```
your-repository/
│
├── .github/
│   ├── workflows/
│       ├── deploy-test.yaml
│
├── helm/
│   ├── rick-and-morty-api/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           ├── ingress.yaml
│
├── yamls/
│   ├── Deployment.yaml
│   ├── Service.yaml
│   ├── Ingress.yaml
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── README.md
```

---

## Testing
- Run the `/healthcheck` endpoint to verify the application is running.
- Query the `/fetch_characters` endpoint with valid parameters to validate functionality.

---

## Troubleshooting
1. **Ingress Issues**:
   - Ensure `minikube tunnel` is running if using Minikube on Docker.
   - Verify the `nginx-ingress` controller is installed and running:
     ```bash
     kubectl get pods -n ingress-nginx
     ```

2. **Helm Errors**:
   - Check if the Helm release already exists:
     ```bash
     helm list
     ```
   - If it does, uninstall it before re-installing:
     ```bash
     helm uninstall rick-and-morty-api
     ```
