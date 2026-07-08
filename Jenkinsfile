pipeline {
    agent any

    stages {
        stage('Test Backend (Flask)') {
            steps {
                checkout scm

                dir('saleapppractice/saleapp') {
                    sh 'python3 demo.py'
                }
            }
        }
    }
}