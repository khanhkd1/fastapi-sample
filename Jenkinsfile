pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "echo 'Building..'"
                sh "docker-compose up -d docker-compose.yml"
            }
        }
    }
}