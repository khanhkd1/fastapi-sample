pipline {
    agent none
    
    stages {
        stage('Build') {
            steps {
                sh "docker-compose up -d docker-compose.yml"
            }
        }
    }
}