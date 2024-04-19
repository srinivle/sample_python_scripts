import boto3
import pandas as pd
from pprint import pprint
from io import StringIO
from datetime import datetime, date
from dateutil.tz import *
from dateutil import relativedelta

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
client3 = session.client('rekognition')

#Detects Labels and Confidence Score from the image uploaded in the given S3 bucket 
response = client3.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'sample88563',
            'Name': 'EventBridge Pipes screenshot.jpg',
        },
    },
    MaxLabels=123,
    MinConfidence=80,
)

a = []
for each in range(0,len(response['Labels'])):
    b = []
    b.append(response['Labels'][each]['Categories'][0]['Name'])
    b.append(response['Labels'][each]['Name'])
    b.append(response['Labels'][each]['Confidence'])
    a.append(b)

pprint(a)

#------------------------------------------------------------------------------------------------
# Detects Text and Confidence Score from the image uploaded in the given S3 bucket
response1 = client3.detect_text(
    Image={
        
        'S3Object': {
            'Bucket': 'sample88563',
            'Name': 'SQS Screenshot.jpg',
            
        }
    },
    Filters={
        'WordFilter': {
            'MinConfidence': 70,
            
        },
        
    }
)

c = []
for each in range(0,len(response1['TextDetections'])):
    d = []
    d.append(response1['TextDetections'][each]['Confidence'])
    d.append(response1['TextDetections'][each]['DetectedText'])
    d.append(response1['TextDetections'][each]['Type'])
    c.append(d)

pprint(c)