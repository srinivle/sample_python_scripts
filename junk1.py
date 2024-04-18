import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
client3 = session.resource('ec2')
'''
response1 = client2.describe_volumes(
                        VolumeIds=[
                        'vol-00c1c38e29202cb7a',
                        'vol-018cce0c1a15e2195',
                        'vol-026af86250afff292',
                    ],
                )

pprint(response1)
'''
response2 = client2.describe_snapshots(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Dev',
            ]
        },
    ],
)

p = response2
pprint(p)
c = []
for each in range(0,len(response2['Snapshots'])):
    b = []
    b.append(response2['Snapshots'][each]['SnapshotId'])
    b.append(response2['Snapshots'][each]['StartTime'])
    b.append(response2['Snapshots'][each]['State'])
    b.append(response2['Snapshots'][each]['StorageTier'])
    b.append(response2['Snapshots'][each]['VolumeId'])
    b.append(response2['Snapshots'][each]['VolumeSize'])
    b.append(response2['Snapshots'][each]['Tags'][0]['Key'])
    b.append(response2['Snapshots'][each]['Tags'][0]['Value'])
    c.append(b)

pprint(c)

'''
from pprint import pprint

def list_in_list(b):
        outside_list = []
        for each in range(0,b):
            inside_list = []      
            
            response1 = client2.describe_instances(
                                InstanceIds=[
                                    df['instance-id'].values[each],
                                ],
                                )
            
            inside_list.append(each)
            inside_list.append(each+1)
            inside_list.append(each+2)
            
            inside_list.append(response1['Reservations'][0]['Instances'][0]['InstanceType'])    
            inside_list.append(response1['Reservations'][0]['Instances'][0]['PrivateIpAddress'])
            inside_list.append(response1['Reservations'][0]['Instances'][0]['RootDeviceType'])
            inside_list.append(response1['Reservations'][0]['Instances'][0]['State']['Name'])
            
            outside_list.append(inside_list)
        return outside_list

a = list_in_list(5)

pprint(a)
'''