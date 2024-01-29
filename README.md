# Python and Redis Demo

This project demonstrates creating a Dockerized Python application with Redis
for learning concepts like:

- Dockerizing Python apps
- Running Redis in containers
- Kubernetes deployments
- Inter-service communication

## Implementation

The app uses:

- Flask as the Python web framework
- Redis as an in-memory data store
- Docker & Docker Compose for local development
- Kubernetes for orchestrated deployments

Key components:

- `app.py` - Flask app that exposes APIs to manage data
- `Dockerfile` - Packages app as a Docker image
- `docker-compose.yml` - Runs app and Redis containers locally
- `k8s/` - Kubernetes resource definitions

## Running the App

### Local Setup

Start full environment locally:

```
docker-compose up
```

### Kubernetes Cluster

Deploy to any Kubernetes cluster:

```
kubectl apply -f k8s/
```

## Potential Additions

Aspects that can be enhanced:

- Production-grade Redis setup
- CI/CD pipelines to manage deployments
- Monitoring, logging, and alerts

This covers the core ideas of containerizing and deploying a Python microservice
app. Many aspects can be built up further for production readiness.
