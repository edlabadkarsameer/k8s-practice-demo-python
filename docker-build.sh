docker build -t backend:latest backend/
docker tag backend:latest edlabadkarsameer/k8s-practice-backend:v1
docker push edlabadkarsameer/k8s-practice-backend:v1

docker build -t frontend:latest frontend/
docker tag frontend:latest edlabadkarsameer/k8s-practice-frontend:v4
docker push edlabadkarsameer/k8s-practice-frontend:v4