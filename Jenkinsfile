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
                sh "docker-compose up docker-compose.yaml -d"
            }
        }
    }
}