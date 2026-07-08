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
                sh 'cd saleapppractice/saleapp'
                sh 'python3 demo.py'
            }
        }
        stage('Deploy lên Vercel') {
            steps {
                // Đổi 'bat' thành 'sh'
                sh 'npm install -g vercel'
                sh 'vercel --token $VERCEL_TOKEN --prod --yes'
            }
        }
    }
}