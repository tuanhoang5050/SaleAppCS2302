pipeline {
    agent any
    tools {
        nodejs 'node'
    }
    environment {
        VERCEL_TOKEN = credentials('VERCEL_AUTH_TOKEN')
    }
    stages {
        stage('Test Backend (Flask)') {
            steps {

                checkout scm
                bat 'cd saleapppractice/saleapp'
                bat 'python demo.py' //
            }
        }
        stage('Deploy lên Vercel') {
            steps {
                bat 'npm install -g vercel'
                bat 'vercel --token %VERCEL_TOKEN% --prod --yes'
            }
        }
    }
}