pipeline {
agent any

stages {

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t arjunkrsharma/flask-devops-app:latest .'
        }
    }
}

}

