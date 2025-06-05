pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        S3_BUCKET = 'image-upload-devops-ravi'
        FUNCTION_NAME = 'imageUploadFunction'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "✅ Cloned from GitHub"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install --upgrade pip
                pip3 install -r requirements.txt -t ./package
                '''
            }
        }

        stage('Package Lambda Function') {
            steps {
                sh '''
                cp lambda_function.py package/
                cd package
                zip -r ../function.zip .
                cd ..
                '''
            }
        }

        stage('Deploy to Lambda') {
            steps {
                sh '''
                aws lambda update-function-code \
                    --function-name $FUNCTION_NAME \
                    --zip-file fileb://function.zip \
                    --region $AWS_REGION
                '''
            }
        }
    }
}
