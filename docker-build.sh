docker build -t backend:latest backend/
docker tag backend:latest edlabadkarsameer/k8s-practice-backend:latest
docker push edlabadkarsameer/k8s-practice-backend:latest

docker build -t frontend:latest frontend/
docker tag frontend:latest edlabadkarsameer/k8s-practice-frontend:v2
docker push edlabadkarsameer/k8s-practice-frontend:v2