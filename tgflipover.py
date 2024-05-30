import boto3
import pandas as pd
from pprint import pprint
from io import StringIO
from datetime import datetime, date
from dateutil.tz import *
from dateutil import relativedelta

session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
client3 = session.client('elbv2')
client4 = session.client('autoscaling')

a = []
b = []
for each in range(2):
    response = client4.describe_auto_scaling_instances()
    a.append(response['AutoScalingInstances'][each]['InstanceId'])
    

pprint(a)

response3 = client3.describe_target_groups()
for each in range(2):
    response1 = client2.describe_instances(
        
        InstanceIds=[
            a[each],
        ],
    )
    for each1 in range(8):
        if response1['Reservations'][0]['Instances'][0]['Tags'][each1].get('Key') == 'Name' and response1['Reservations'][0]['Instances'][0]['Tags'][each1].get('Value') == 'blue':
            response2 = client3.deregister_targets(
                TargetGroupArn=response3['TargetGroups'][0]['TargetGroupArn'],
                Targets=[
                    {
                        'Id': a[each],
                        
                    },
                ]
            )

            pprint("Successfully deregistered the target")

        elif response1['Reservations'][0]['Instances'][0]['Tags'][each1].get('Key') == 'Name' and response1['Reservations'][0]['Instances'][0]['Tags'][each1].get('Value') == 'green': 
            response2 = client3.register_targets(
                TargetGroupArn=response3['TargetGroups'][0]['TargetGroupArn'],
                Targets=[
                    {
                        'Id': a[each],
                        
                    },
                ]
            )
            pprint("Successfully registered the target")
