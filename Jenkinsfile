pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/arjunkrsharma/jenkins-cicd-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t arjunkrsharma/flask-devops-app:latest .'
            }
        }
    }
}
