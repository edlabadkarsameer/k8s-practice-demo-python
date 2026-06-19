pipeline {

agent any

parameters {

    choice(
        name: 'ENV',
        choices: ['DEV', 'UAT', 'PROD'],
        description: 'Select Environment'
    )

    booleanParam(
        name: 'RUN_SCAN',
        defaultValue: true,
        description: 'Run Security Scan'
    )

    string(
        name: 'VERSION',
        defaultValue: '1.0.0',
        description: 'Application Version'
    )
}

stages {

    stage('Show Parameters') {

        steps {

            echo "Environment: ${params.ENV}"
            echo "Version: ${params.VERSION}"
            echo "Run Scan: ${params.RUN_SCAN}"
        }
    }

    stage('Build') {

        steps {

            echo "Building Application..."
        }
    }

    stage('Security Scan') {

        when {

            expression {
                return params.RUN_SCAN
            }
        }

        steps {

            echo "Running Security Scan..."
        }
    }

    stage('Approval') {

        steps {

            input(
                message: 'Deploy Application?',
                ok: 'Deploy'
            )
        }
    }

    stage('Deploy DEV') {

        when {

            expression {
                return params.ENV == 'DEV'
            }
        }

        steps {

            echo "Deploying to DEV"
        }
    }

    stage('Deploy UAT') {

        when {

            expression {
                return params.ENV == 'UAT'
            }
        }

        steps {

            echo "Deploying to UAT"
        }
    }

    stage('Deploy PROD') {

        when {

            expression {
                return params.ENV == 'PROD'
            }
        }

        steps {

            echo "Deploying to PROD"
        }
    }
}

post {

    success {

        echo "Pipeline Success"
    }

    failure {

        echo "Pipeline Failed"
    }

    always {

        echo "Cleanup Activities"
    }
}

}
