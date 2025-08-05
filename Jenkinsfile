pipeline {
    agent any

    environment {
        IMAGE_NAME = "quiz-app"
        CONTAINER_NAME = "quiz-app-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo-name.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Stop and Remove Existing Container') {
            steps {
                script {
                    // Stop and remove old container if exists
                    sh """
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
                }
            }
        }
    }
}

