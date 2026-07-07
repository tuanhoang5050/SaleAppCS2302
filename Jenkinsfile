pipeline {
    agent any 

    stages {
        stage('Bước 1: Kéo Code (Checkout)') {
            steps {
   
                checkout scm 
            }
        }
        
        stage('Bước 2: Chạy Demo (Test)') {
            steps {
                dir('saleapppractice/saleapp') {
                    bat 'python demo.py' 
                }
            }
        }
    }
}