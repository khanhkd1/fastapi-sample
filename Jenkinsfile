pipeline {
    agent {
        node {
            label 'Build'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh "echo 'Building..'"
                sh "/usr/local/bin/docker --version"
                sh "/usr/local/bin/docker-compose --version"
                sh "/usr/local/bin/docker-compose up -d docker-compose.yml"
            }
        }
    }
}