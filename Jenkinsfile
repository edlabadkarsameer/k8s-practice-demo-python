pipeline {

```
agent any

parameters {

    choice(
        name: 'ENV',
        choices: ['DEV', 'UAT', 'PROD'],
        description: 'Select environment'
    )

    string(
        name: 'VERSION',
        defaultValue: '1.0'
    )
}

stages {

    stage('Test') {

        steps {

            echo "Environment = ${params.ENV}"
            echo "Version = ${params.VERSION}"
        }
    }
}
```

}
