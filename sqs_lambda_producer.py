import json
import boto3
import random
import uuid
from datetime import datetime, timedelta

sqs_client = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/471112663332/AirbnbBookingQueue'  # replace with your SQS Queue URL
BOOKING_START = datetime(2022, 1, 1)

def generate_random_booking_time():
    random_days_start = random.randint(0, 100)
    random_days_end = random.randint(0, 100)
    random_start_date = (BOOKING_START + timedelta(days=random_days_start))
    random_end_date = (random_start_date + timedelta(days=random_days_end))
    return random_start_date, random_end_date

def generate_booking():
    start_date, end_date = generate_random_booking_time()
    
    return {
        "bookingId": str(uuid.uuid4()),
        "userId": random.randint(1000, 9999),
        "propertyId": random.randint(100, 999),
        "location": random.choice(['Fsd, Pakistan', 'Lahore, Pakistan', 'Karachi, Pakistan', 'Islamabad, Pakistan']),
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "price": random.uniform(30, 100)
    }
 

def lambda_handler(event, context):
    i=0
    while(i<5):
        customer_booking = generate_booking()
        print(customer_booking)
        
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(customer_booking)
        )
        i += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Booking data published to SQS!')
    }