pipeline {
    agent any
    environment {
        IMAGE_NAME = "afrahali26/food-delivery"
        K8S_DEPLOYMENT = "food-delivery"
        K8S_CONTAINER = "food-delivery"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Test') {
            steps {
                sh """
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    pytest -q
                """
            }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .' }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$BUILD_NUMBER
                        docker logout
                    """
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh """
                    kubectl set image deployment/$K8S_DEPLOYMENT $K8S_CONTAINER=$IMAGE_NAME:$BUILD_NUMBER
                    kubectl rollout status deployment/$K8S_DEPLOYMENT --timeout=180s
                """
            }
        }
    }
    post {
        always { sh 'docker image prune -f || true' }
    }
}
