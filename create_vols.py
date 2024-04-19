import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')

a = []
for each in range(0,5):
    response = client2.create_volume(
                    AvailabilityZone='us-east-1a',
                    Size=1,
                    VolumeType='gp3',
                    TagSpecifications=[
                        {
                            'ResourceType': 'volume',
                            'Tags': [
                                {
                                    'Key': 'env',
                                    'Value': 'Prod'
                                },
                            ]
                        },
                    ],
                )
    a.append(response['VolumeId'])

header = ['volume-id']
data = pd.DataFrame(a, columns=header)
data.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\list-of-volumes.csv", index=False)

client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\list-of-volumes.csv', 'sample88563', 'list-of-volumes.csv')
print(" Successfully uploaded the 'list of volumes' file to AWS S3 bucket ")
