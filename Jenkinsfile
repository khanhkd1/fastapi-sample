pipeline {
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    stages {
        stage('Build') {
            steps {
                sh "echo 'Building..'"
                sh "docker-compose up -d docker-compose.yml"
            }
        }
    }
}