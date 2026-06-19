pipeline {

```
agent any

parameters {

    choice(
        name: 'ENV',
        choices: "DEV\nUAT\nPROD",
        description: 'Select Environment'
    )
}

stages {

    stage('Test') {

        steps {

            echo "Selected ENV: ${params.ENV}"
        }
    }
}
```

}
