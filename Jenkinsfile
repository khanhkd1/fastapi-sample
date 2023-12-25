pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:$PATH"
    }
    stages {
        stage('Build') {
            steps {
                sh "docker-compose up -d docker-compose.yml"
            }
        }
    }
}