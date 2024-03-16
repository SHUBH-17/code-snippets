import json
import boto3
import random
import datetime

sqs_client = boto3.client('sqs')
QUEUE_URL = 'https:......'  #sqs queue url

def generate_booking_data(n):
    startDate = datetime.date(2024, 3, 1)
    if(n%2==0):
        endDate = startDate + datetime.timedelta(days=random.randint(2, 30))
    else:
        endDate = startDate + datetime.timedelta(days=1)
    
    stayDuration = endDate - startDate
    stayDuration = stayDuration.days
    
    # List of cities.
    cities = ['Gorakhpur','New York', 'London', 'Paris', 'Tokyo', 'Sydney']
    # List of countries.
    countries = ['Bharat','United States', 'United Kingdom', 'France', 'Japan', 'Australia']
    city_index = random.randint(0, len(cities) - 1)
    country_index = random.randint(0, len(countries) - 1)
    location = cities[city_index] + ', ' + countries[country_index]
 
    return {
        "bookingId": random.randint(1000, 9999),
        "userId": random.randint(100, 999),
        "propertyId": random.randint(1, 100),
        "location": location,
        "startDate": startDate,
        "endDate": endDate,
        "stayDuration" : stayDuration,
        "price": round(random.uniform(100.0, 5000.0), 2)
    }
	
def lambda_handler(event, context):
    i=1
    while(i<=5):
        booking_data = generate_booking_data(i)
        print(json.dumps(booking_data, default=str))
        
        """
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(booking_data, default=str)
        )
        """
        
        i += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Booking data published to SQS!')
    }
