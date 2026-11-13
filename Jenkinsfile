pipeline {
    agent any

    environment {
        IMAGE_NAME = 'afrahali26/food-delivery'
    }

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/afrahali-xo/food-delivery-devops.git'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Food Delivery Application...'
                sh 'ls -la'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Application Tests...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                        docker push $IMAGE_NAME:$BUILD_NUMBER

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Food Delivery CI/CD Pipeline Completed Successfully!'
        }

        failure {
            echo 'Food Delivery CI/CD Pipeline Failed!'
        }
    }
}
