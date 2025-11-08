pipeline {
    agent any
    stages {

        stage("checkout code") {
            steps {
                checkout scm
            }
        }

        stage("extract Data") {
            steps {

                bat "C:\\Users\\hpeg2\\AppData\\Local\\Programs\\Python\\Python314\\python.exe extract.py"
            }
        }


    }
}