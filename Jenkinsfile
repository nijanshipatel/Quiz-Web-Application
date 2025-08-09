pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub')  // Jenkins credentials ID
        IMAGE_NAME = 'quiz-app'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/nijanshipatel/Quiz-Web-Application.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Tag Image for Docker Hub') {
            steps {
                script {
                    sh 'docker tag $IMAGE_NAME $DOCKERHUB_USR/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    sh 'docker push $DOCKERHUB_USR/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Stop Existing Container') {
            steps {
                script {
                    sh '''
                    docker stop quiz-container || true
                    docker rm quiz-container || true
                    '''
                }
            }
        }

        stage('Run Container from Docker Hub Image') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name quiz-container $DOCKERHUB_USR/$IMAGE_NAME:latest'
                }
            }
        }
    }
}



