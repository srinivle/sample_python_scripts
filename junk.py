import boto3
import pandas as pd
import csv as csv
from pprint import pprint
import numpy as np
import os
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
response1 = client2.describe_instances(
InstanceIds=[
    'i-0949de4c89053cf2e',
],
)
pprint(response1)
df = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sample-junk.csv")
sample_list=[]
sample_list1=[]
pprint(df['instance-id'])
#a = int(len(df))
pprint(len(df))

df.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sample-junk1.csv", index=False)

for each1 in df['instance-id']:
    i = 0
    response1 = client2.describe_instances(
                        InstanceIds=[
                            each1,
                        ],
                        )

    sample_list.append(response1['Reservations'][0]['Instances'][i]['InstanceId'])
    sample_list.append(response1['Reservations'][0]['Instances'][i]['InstanceType'])    
    sample_list.append(response1['Reservations'][0]['Instances'][i]['PrivateIpAddress'])
    sample_list.append(response1['Reservations'][0]['Instances'][i]['RootDeviceType'])
    sample_list.append(response1['Reservations'][0]['Instances'][i]['State']['Name'])
    i = i + 1
    sample_list1.append(sample_list)


pprint(each1)
pprint(sample_list)
pprint(sample_list1)


header = ['InstanceId', 'InstanceType', 'PrivateIpAddress', 'RootDeviceName', 'RootDeviceType']

data = pd.DataFrame(sample_list1, columns=header)
data.to_csv('Stu_data.csv', index=False)

z = os.path.abspath('instance-status.csv')

df1 = pd.read_csv(r"z", usecols=['InstanceId', 'State'])
pprint(df1)
pprint(df1.iloc[3]['State'])

client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\instance-status.csv', 'sample88563', 'instance-status.csv')