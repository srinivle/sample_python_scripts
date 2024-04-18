import samplevolfunc
import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
pprint("Executing Creation of Snapshots")
df1 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\volume-status.csv")
for each3 in range(0,len(df1['VolumeId'])):
        response4 = client2.create_snapshot(
            VolumeId=df1['VolumeId'].values[each3],
            TagSpecifications=[
                {   
                    'ResourceType': 'snapshot', 
                    'Tags': [
                        {
                            'Key': 'Env',
                            'Value': 'Dev'
                        },
                    ]
                },
            ],            
        )