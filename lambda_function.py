import json
import boto3
import base64

s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET_NAME = 'image-upload-devops-ravi'  # ✅ Your S3 bucket
RAW_FOLDER = 'raw/'  # Folder for raw image uploads

# Replace this with your actual SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:261469840250:InvalidImageAlert'

def lambda_handler(event, context):
    print("✅ Lambda function triggered")

    try:
        body = json.loads(event['body'])
        image_data = body.get('image_data')
        file_name = body.get('file_name')

        print(f"📝 Received file: {file_name}")

        # Validate file type
        if not file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            print("❌ Invalid file type")

            # Publish to SNS for alert
            message = f"Invalid image upload attempt: {file_name}"
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="❗ Invalid Image Upload Attempt",
                Message=message
            )

            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid file type. Only .jpg, .jpeg, .png allowed."})
            }

        # Decode and upload image to S3
        image_binary = base64.b64decode(image_data)
        print("✅ Image base64 decoded")

        s3.put_object(Bucket=BUCKET_NAME, Key=RAW_FOLDER + file_name, Body=image_binary)
        print("✅ Image uploaded to S3:", RAW_FOLDER + file_name)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Image uploaded successfully!"})
        }

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
