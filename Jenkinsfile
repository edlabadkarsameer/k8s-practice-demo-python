pipeline {
agent any

parameters {

    choice(
        name: 'ENVIRONMENT',
        choices: ['DEV', 'UAT', 'PROD'],
        description: 'Select Deployment Environment'
    )

    booleanParam(
        name: 'RUN_SECURITY_SCAN',
        defaultValue: true,
        description: 'Run Security Scan'
    )

    booleanParam(
        name: 'DEPLOY',
        defaultValue: true,
        description: 'Deploy Application'
    )
}

environment {

    BACKEND_IMAGE = "edlabadkarsameer/k8s-practice-backend:${BUILD_NUMBER}"

    FRONTEND_IMAGE = "edlabadkarsameer/k8s-practice-frontend:${BUILD_NUMBER}"
}

options {

    disableConcurrentBuilds()

    timeout(
        time: 45,
        unit: 'MINUTES'
    )
}

stages {

    stage('Checkout') {

        steps {

            checkout scm
        }
    }

    stage('Build Images') {

        parallel {

            stage('Build Backend') {

                steps {

                    sh """
                    docker build \
                    -t ${BACKEND_IMAGE} \
                    backend/
                    """
                }
            }

            stage('Build Frontend') {

                steps {

                    sh """
                    docker build \
                    -t ${FRONTEND_IMAGE} \
                    frontend/
                    """
                }
            }
        }
    }

    stage('Security Scan') {

        when {

            expression {
                return params.RUN_SECURITY_SCAN
            }
        }

        steps {

            echo "Running Security Scan"

            sh '''
            echo "Trivy Scan Placeholder"
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
                echo $PASS | docker login \
                -u $USER \
                --password-stdin
                '''
            }
        }
    }

    stage('Push Images') {

        parallel {

            stage('Push Backend') {

                steps {

                    sh """
                    docker push ${BACKEND_IMAGE}
                    """
                }
            }

            stage('Push Frontend') {

                steps {

                    sh """
                    docker push ${FRONTEND_IMAGE}
                    """
                }
            }
        }
    }

    stage('Approval Gate') {

        when {

            expression {

                return params.ENVIRONMENT == 'UAT' ||
                       params.ENVIRONMENT == 'PROD'

            }
        }

        steps {

            input(
                message: "Approve deployment to ${params.ENVIRONMENT} ?",
                ok: "Deploy"
            )
        }
    }

    stage('Deploy') {

        when {

            expression {

                return params.DEPLOY

            }
        }

        steps {

            script {

                if (params.ENVIRONMENT == 'DEV') {

                    echo "Deploying to DEV"

                } else if (params.ENVIRONMENT == 'UAT') {

                    echo "Deploying to UAT"

                } else {

                    echo "Deploying to PROD"

                }
            }

            sh """
            kubectl set image deployment/backend \
            backend=${BACKEND_IMAGE} \
            -n employee-app
            """

            sh """
            kubectl set image deployment/frontend \
            frontend=${FRONTEND_IMAGE} \
            -n employee-app
            """
        }
    }

    stage('Validate Rollout') {

        when {

            expression {

                return params.DEPLOY

            }
        }

        steps {

            sh '''
            kubectl rollout status deployment/backend \
            -n employee-app

            kubectl rollout status deployment/frontend \
            -n employee-app
            '''
        }
    }
}

post {

    success {

        echo "Pipeline Succeeded"
    }

    failure {

        echo "Pipeline Failed"
    }

    aborted {

        echo "Pipeline Aborted"
    }

    always {

        sh 'docker logout || true'
    }
}
}
