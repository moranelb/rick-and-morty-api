# Rick and Morty REST API Kubernetes Deployment with Helm

## Kubernetes Deployment with Helm

This guide covers deploying the Rick and Morty REST API using a Helm chart.

---

### Prerequisites

- Minikube running locally with Docker as the driver.
- Docker installed and configured.
- Helm installed and set up.

---

### Steps to Deploy Using Helm

1. **Navigate to the Helm chart directory**:
   ```bash
   cd helm/rick-and-morty-api
   ```

2. **Deploy the Helm chart**:
   ```bash
   helm install rick-and-morty-api .
   ```

3. **Verify the deployment**:
   - Check the pods:
     ```bash
     kubectl get pods
     ```
   - Check the services:
     ```bash
     kubectl get svc
     ```
   - Check the ingress:
     ```bash
     kubectl get ingress
     ```

4. **If using Minikube with Docker**:
   - Run the following command to enable the Minikube tunnel:
     ```bash
     minikube tunnel
     ```
   - Keep the terminal running as the tunnel must remain active.

5. **Configure local `/etc/hosts` file**:
   - Add the following entry:
     ```plaintext
     127.0.0.1 rick-and-morty.local
     ```

6. **Access the application**:
   - Open [http://rick-and-morty.local](http://rick-and-morty.local) in your browser.

---

### Helm Values Configuration

The `values.yaml` file allows customizing the deployment. Below are the configurable parameters:

| Parameter         | Description                               | Default Value          |
|-------------------|-------------------------------------------|------------------------|
| `image.repository`| Docker image repository                  | `moranelb/rick-and-morty-api` |
| `image.tag`       | Docker image tag                         | `latest`              |
| `replicaCount`    | Number of replicas                       | `1`                   |
| `service.type`    | Kubernetes service type                  | `NodePort`            |
| `service.port`    | Service port exposed                     | `80`                  |
| `ingress.enabled` | Enable/Disable Ingress                   | `true`                |
| `ingress.host`    | Hostname for the Ingress                 | `rick-and-morty.local`|

---

### Verify Application Endpoints

- Healthcheck: [http://rick-and-morty.local/healthcheck](http://rick-and-morty.local/healthcheck)
- Fetch Characters: [http://rick-and-morty.local/fetch_characters?species=<species>&status=<status>&origin=<origin>](http://rick-and-morty.local/fetch_characters?species=<species>&status=<status>&origin=<origin>)
``` 