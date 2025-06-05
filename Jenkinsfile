pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        S3_BUCKET = 'your-s3-bucket-name'           // Replace with your actual S3 bucket name
        FUNCTION_NAME = 'your-lambda-function-name' // Replace with your actual Lambda function name
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "✅ Cloned from GitHub"
                // SCM checkout is automatic before this stage in declarative pipeline with 'Pipeline script from SCM'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Update package list - non-fatal if fails
                apt update || true

                # Install zip utility if not present - non-fatal if fails
                apt install zip -y || true

                # Upgrade pip
                pip install --upgrade pip

                # Install Python requirements to package directory
