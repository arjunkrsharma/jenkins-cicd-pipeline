pipeline {
agent any

environment {
    DOCKER_IMAGE = "arjunkrsharma/flask-devops-app"
}

stages {

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t $DOCKER_IMAGE:latest .'
        }
    }

    stage('Push To DockerHub') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh '''
                echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                docker push $DOCKER_IMAGE:latest
                '''
            }
        }
    }
}

}

