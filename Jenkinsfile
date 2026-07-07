pipeline {
    agent any
    stages {
        stage('Chuẩn bị Code') {
            steps {
                git 'https://github.com/tuanhoang5050/SaleAppCS2302.git'
            }
        }
        stage('Chạy thử nghiệm Demo') {
            steps {
                bat 'cd saleapppractice\\saleapp'
                bat 'python demo.py'
            }
        }
    }
}