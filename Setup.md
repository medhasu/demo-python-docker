# Technical Details

This project uses
[flask Webframework](https://flask.palletsprojects.com/en/1.1.x/) and
[redis](https://redis.io/) to cover the following points.

Note: This project created for testing purpose and it is not production ready
:-)

## Prerequisites

THis project requires the following Prerequisites

- Python
- Docker Desktop
- Kubernets enable in Docker Desktop

## Setup local database

Docker offers application virtualization as container. This project requires
redis database.

Here are few sample docker command to run redis server and interact with it.

1. Run the Redis Docker that expose service in port `6379` which will be
   accessed through `8001` in host application

```bash
docker run --name test-redis-container -p 8001:6379 -d redis
```

If container stopped then you can start it through

```bash
docker start test-redis-container
```

to read logs

```
docker container logs --tail 100 test-redis-container
```

2. To list running containers

```bash
docker ps
```

3. login redis server

```bash
docker exec -it test-redis-container bash
```

## Prepare Dev System

```py
python3 -m venv ~/ws/py3/env # Create Env
source ~/ws/py3/env/bin/activate # Activate Env
easy_install pip  # Install pip in virtual env
```

## How to test

```
source ~/ws/py3/env/bin/activate
python app.py
```

Create one item through `curl`

```bash
curl -X POST -F key="test1" -F val="val1"  http://127.0.0.1:8009/items
```

You can verify result in http://127.0.0.1:8009/items and you can observe the
data is populated through url

## How to Deploy Test Application using docker Compose

The following steps involves

1. Create Dockerfile for Python App
2. Create Docker Image
3. Create Docker Compose file
4. Test

## Step 1: Create Docker file

```dockerfile
FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8009
CMD [ "python3", "app.py"]
```

### Step 2: Create Image

you can build docker image like python-web-test

```bash
docker build . -t python-web-test
```

### Step 3:

create compose file like `docker-compose.yml`

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8009:8009"
    environment:
       - REDIS_HOST=redis
       - REDIS_PORT=6379
    links:
       - "redis:redis"
  redis:
    image: "redis:alpine"
```

To rebuild image when there is change in `app.py`

```bash
docker-compose build --no-cache
```

### Step 4:

```bash
docker-compose up
```

Open the following test link in brower http://localhost:8009/items

Create Test data like

## Test Kubernetes with minikube

install https://minikube.sigs.k8s.io/docs/start/

```
eval $(minikube -p minikube docker-env)
```

```bash
kubectl apply -f kubernet/redis-deployment.yaml 
export REDISHOST_IP=172.17.0.5
kubectl create configmap redishost --from-literal=REDISHOST=${REDISHOST_IP}

kubectl apply -f kubernet/webapp-deployment.yaml
```

```
kubectl expose deployment webapp --type=LoadBalancer --port=8009
```

```
minikube service  webapp
```

```
minikube addons list
```

kubectl get pod,svc -n kube-system

## References

- https://docs.docker.com/language/python/build-images/
- https://docs.python.org/3/library/venv.html#module-venv &
  https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
- https://minikube.sigs.k8s.io/docs/start/
