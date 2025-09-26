pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tanay9911/scientific-calculator.git'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t tanay9911/scientific-calculator:latest .'
            }
        }
        stage('Docker Push') {
            steps {
                sh 'docker push tanay9911/scientific-calculator:latest'
            }
        }
    }
}
