pipeline {

```
agent any

parameters {

    choice(
        name: 'ENVIRONMENT',
        choices: ['DEV', 'UAT', 'PROD'],
        description: 'Select deployment environment'
    )

    booleanParam(
        name: 'RUN_SECURITY_SCAN',
        defaultValue: true,
        description: 'Run security scan?'
    )

    string(
        name: 'VERSION',
        defaultValue: '1.0.0',
        description: 'Application version'
    )
}

environment {

    APP_NAME = "employee-app"
    OWNER = "sameer"
}

options {

    disableConcurrentBuilds()

    timeout(
        time: 30,
        unit: 'MINUTES'
    )

    buildDiscarder(
        logRotator(
            numToKeepStr: '10'
        )
    )
}

stages {

    stage('Display Parameters') {

        steps {

            echo "Environment: ${params.ENVIRONMENT}"
            echo "Version: ${params.VERSION}"
            echo "Owner: ${OWNER}"
        }
    }

    stage('Parallel Jobs') {

        parallel {

            stage('Frontend Build') {

                steps {

                    echo "Building frontend..."
                }
            }

            stage('Backend Build') {

                steps {

                    echo "Building backend..."
                }
            }
        }
    }

    stage('Conditional Stage') {

        when {

            expression {

                params.RUN_SECURITY_SCAN

            }
        }

        steps {

            echo "Running security scan..."
        }
    }

    stage('Retry Example') {

        steps {

            retry(3) {

                echo "Trying operation..."
            }
        }
    }

    stage('Script Block') {

        steps {

            script {

                def buildType = "Release"

                echo "Build Type: ${buildType}"
            }
        }
    }

    stage('Manual Approval') {

        steps {

            timeout(
                time: 1,
                unit: 'MINUTES'
            ) {

                input(
                    message: 'Approve deployment?',
                    ok: 'Deploy'
                )
            }
        }
    }

    stage('Deploy DEV') {

        when {

            expression {

                params.ENVIRONMENT == 'DEV'

            }
        }

        steps {

            echo "Deploying to DEV"
        }
    }

    stage('Deploy UAT') {

        when {

            expression {

                params.ENVIRONMENT == 'UAT'

            }
        }

        steps {

            echo "Deploying to UAT"
        }
    }

    stage('Deploy PROD') {

        when {

            expression {

                params.ENVIRONMENT == 'PROD'

            }
        }

        steps {

            echo "Deploying to PROD"
        }
    }

    stage('Credentials Example') {

        steps {

            withCredentials([
                usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )
            ]) {

                echo "Using credentials securely"
            }
        }
    }

    stage('Downstream Job Example') {

        steps {

            echo "Triggering another Jenkins job"

            // build job: 'Deploy-Application'
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

        echo "Cleanup Tasks"
    }
}
```

}
