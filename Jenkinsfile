pipeline {
    agent {
        node {
            label 'Build'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh "echo 'Building.. and push to Docker Hub'"
                // sh "docker-compose up -d"
                sh "docker build -t khanhkieu167/fastapi-sample:latest -f app/Dockerfile ."
                sh "docker login -u khanhkieu167 -p dckr_pat_qVsUDqy20ERNtoXUnX2WdiPGN2Q"
                sh "docker push khanhkieu167/fastapi-sample:latest"
            }
        }
    }
}