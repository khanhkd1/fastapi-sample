pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "echo 'Building..'"
                sh "docker --version"
                sh "docker-compose --version"
                sh "docker-compose up -d docker-compose.yml"
            }
        }
    }
}