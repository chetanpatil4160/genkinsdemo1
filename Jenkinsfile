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

                bat "python extract.py"
            }
        }


    }
}