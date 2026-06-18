pipeline {

    agent any

    environment {

        DOCKER_USER_BACKEND = "edlabadkarsameer/k8s-practice-backend"
        DOCKER_USER_FRONTEND = "edlabadkarsameer/k8s-practice-frontend"

    }

    stages {

        stage('Checkout') {

            steps {
                checkout scm
            }
        }

        stage('Build Backend') {

            steps {

                sh '''
                docker build \
                -t $DOCKER_USER_BACKEND:${BUILD_NUMBER} \
                backend/
                '''
            }
        }

        stage('Build Frontend') {

            steps {

                sh '''
                docker build \
                -t $DOCKER_USER_FRONTEND:${BUILD_NUMBER} \
                frontend/
                '''
            }
        }

        stage('Docker Login') {

            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Backend') {

            steps {

                sh '''
                docker push $DOCKER_USER_BACKEND:${BUILD_NUMBER}
                '''
            }
        }

        stage('Push Frontend') {

            steps {

                sh '''
                docker push $DOCKER_USER_FRONTEND:${BUILD_NUMBER}
                '''
            }
        }

        stage('Deploy') {

            steps {

                sh '''
                kubectl set image deployment/backend \
                backend=$DOCKER_USER_BACKEND:${BUILD_NUMBER} \
                -n employee-app

                kubectl set image deployment/frontend \
                frontend=$DOCKER_USER_FRONTEND:${BUILD_NUMBER} \
                -n employee-app
                '''
            }
        }
    }
}