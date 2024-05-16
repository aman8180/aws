pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build('test aws', '.')
                }
            }
        }
        
        stage('Push to AWS ECR') {
            steps {
                script {
                    // Push Docker image to AWS ECR
                    docker.withRegistry('https://975050170236.dkr.ecr.ap-south-1a.amazonaws.com', 'aws-jenkins') {
                        docker.image('test aws').push('latest')
                    }
                }
            }
        }
        
        stage('Deploy Lambda Function') {
            steps {
                script {
                    // Deploy Lambda function
                    sh 'aws lambda update-function-code --function-name run-jenkins --image-uri public.ecr.aws/o6f7w8w9/jenkinsrepo:latest'
                }
            }
        }
    }
}
