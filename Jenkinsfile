pipeline {

 agent any

 stages {

  stage('Git Checkout') {

   steps {
    git 'https://github.com/user/repo.git'
   }
  }

  stage('Build Backend') {

   steps {
    sh 'docker build -t backend:latest backend/'
   }
  }

  stage('Build Frontend') {

   steps {
    sh 'docker build -t frontend:latest frontend/'
   }
  }

  stage('Push Images') {

   steps {

    sh '''
    docker tag backend:latest edlabadkarsameer/k8s-practice-backend:latest
    docker push edlabadkarsameer/k8s-practice-backend:latest

    docker tag frontend:latest edlabadkarsameer/k8s-practice-frontend:latest
    docker push edlabadkarsameer/k8s-practice-frontend:latest
    '''
   }
  }

  stage('Deploy') {

   steps {

    sh '''
    kubectl apply -f kubernetes/
    '''
   }
  }
 }
}