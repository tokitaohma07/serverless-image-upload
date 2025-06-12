pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        S3_BUCKET = 'image-upload-devops-ravi'
        LAMBDA_FUNCTION = 'imageUploadFuntion'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/tokitaohma07/serverless-image-upload.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Package Lambda Function') {
            steps {
                sh '''
                    zip -r function.zip lambda_function.py
                '''
            }
        }

        stage('Upload to S3') {
            steps {
                sh '''
                    aws s3 cp function.zip s3://$S3_BUCKET/function.zip --region $AWS_REGION
                '''
            }
        }

        stage('Deploy to Lambda') {
            steps {
                sh '''
                    aws lambda update-function-code \
                        --function-name $LAMBDA_FUNCTION \
                        --s3-bucket $S3_BUCKET \
                        --s3-key function.zip \
                        --region $AWS_REGION
                '''
            }
        }
    }
}
