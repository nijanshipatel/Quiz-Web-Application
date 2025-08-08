pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/nijanshipatel/Quiz-Web-Application.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t quiz-app .'
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

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name quiz-container quiz-app'
                }
            }
        }
    }
}


