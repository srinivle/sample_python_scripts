import samplevolfunc
import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')

df = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\list-of-volumes.csv")
b = len(df)
pprint("We are creating Tags for Volumes here")
a = input("Enter the Tag Key for the resource: ")
c = input("Enter the Tag Value for the resource: ")

# Creation of Tags for Volumes
for each in range(0,b):
    response1 = client2.create_tags(                    
                    Resources=[
                        df['volume-id'].values[each],
                    ],
                    Tags=[
                        {
                            'Key': a,
                            'Value': c
                        },
                    ]
                )
pprint(response1)