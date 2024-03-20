import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Extract event data (assuming it's JSON)
    event_data = json.dumps(event)
    
    # Define S3 bucket and object key
    bucket_name = 'airbnb-booking-records-ar'
    object_key = f'events/{datetime.now().isoformat()}.json'  # Example: events/2024-03-20T12:00:00.json
    
    try:
        # Write event data to S3 object
        s3.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=event_data,
            ContentType='application/json'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Event data written to S3 successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }