# Food Delivery DevOps Demo

A small food-ordering demo for practising an end-to-end DevOps pipeline.

## Flow
GitHub -> Jenkins -> pytest -> Docker -> Docker Hub -> Kubernetes (EKS)

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app/app.py
```
Open http://localhost:5000. Health check: http://localhost:5000/health

## Run with Docker
```bash
docker build -t food-delivery:local .
docker run --rm -p 5000:5000 food-delivery:local
```
Or: `docker compose up --build`

## First Kubernetes deployment
1. Replace YOUR_DOCKERHUB_USERNAME in `k8s/deployment.yaml` and `Jenkinsfile`.
2. Push an image to Docker Hub and update the image in the manifest.
3. Ensure kubectl is connected to your cluster.
4. Apply once before the first Jenkins deployment:
```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get svc food-delivery-service
```
A LoadBalancer Service on EKS can incur AWS charges. Clean up with `kubectl delete -f k8s/`.

## Jenkins prerequisites
The Jenkins agent needs Git, Python 3 + venv, Docker CLI/daemon, and kubectl configured for the cluster.
Create a Jenkins Username with password credential with ID `dockerhub-creds`.
Create a Pipeline job pointing to this GitHub repository. Configure a GitHub webhook to trigger builds.
Update IMAGE_NAME in the Jenkinsfile. The pipeline assumes the Kubernetes Deployment already exists.

## Scope
This is a learning demo only. It does not process real payments, store customer data, or connect to a real delivery network. Never commit passwords, access keys, or tokens.
