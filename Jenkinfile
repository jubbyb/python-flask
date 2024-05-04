pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build('my-docker-image:${env.BUILD_NUMBER}')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run('-p 5000:5000 -d')
                }
            }
        }
    }

    post {
        always {
            script {
                dockerImage.stop()
                dockerImage.remove()
            }
        }
    }
}