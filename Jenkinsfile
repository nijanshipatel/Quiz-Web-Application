pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t quiz-app:latest .'
            }
        }
        stage('Done') {
            steps {
                echo 'Pipeline complete.'
            }
        }
    }
}
