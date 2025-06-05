pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        S3_BUCKET = 'image-upload-devops-ravi'
        FUNCTION_NAME = 'imageUploadFunction'
        VENV_DIR = '.venv'
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
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                $VENV_DIR/bin/pip install --upgrade pip
                $VENV_DIR/bin/pip install -r requirements.txt -t ./package
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
