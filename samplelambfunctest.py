import json
import boto3
from pprint import pprint
# def lambda_handler(event, context):
    # TODO implement
'''    
client0 = boto3.client('sts')
response = client0.assume_role(RoleArn='arn:aws:iam::058264069674:role/service-role/samplefunctest-role-v2rjprd0', RoleSessionName='samplefunctest-role-v2rjprd0')
acc1 = response['Credentials']['AccessKeyId']
acc2 = response['Credentials']['SecretAccessKey']
'''    
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('ec2')
response1 = client1.describe_instances(
InstanceIds=[
    'i-0949de4c89053cf2e',
],
)
pprint(response1['Reservations'][0]['Instances'][0]['State']['Name'])
if (response1['Reservations'][0]['Instances'][0]['State']['Name'] == 'stopped'):
    response2 = client1.start_instances(
                    InstanceIds=[
                        'i-0949de4c89053cf2e',
                    ])
    pprint("We are starting the Instance id "+response2['StartingInstances'][0]['InstanceId']+ " is "+response2['StartingInstances'][0]['CurrentState']['Name']+" as earlier it was "+response2['StartingInstances'][0]['PreviousState']['Name'])
else: 
    response3 = client1.stop_instances(
                    InstanceIds=[
                        'i-0949de4c89053cf2e',
                    ])
    pprint("We are stopping the Instance id "+response3['StoppingInstances'][0]['InstanceId']+ " is "+response3['StoppingInstances'][0]['CurrentState']['Name']+" as earlier it was "+response3['StoppingInstances'][0]['PreviousState']['Name'])
    
    # return