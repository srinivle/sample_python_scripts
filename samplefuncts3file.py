import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')

# Reading the Object using Pandas
response = client1.get_object(Bucket='sample88563', Key='running-instances.csv')
data = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(data))

# Total number of Objects in CSV File
b = len(df)


# Creating List in Lists to Supply DataFrame
outside_list = []
for each in range(0,b):
    inside_list = []      
    response1 = client2.describe_instances(
                        InstanceIds=[
                            df['instance-id'].values[each],
                        ],
                        )

    inside_list.append(response1['Reservations'][0]['Instances'][0]['InstanceId'])
    inside_list.append(response1['Reservations'][0]['Instances'][0]['InstanceType'])    
    inside_list.append(response1['Reservations'][0]['Instances'][0]['PrivateIpAddress'])
    inside_list.append(response1['Reservations'][0]['Instances'][0]['RootDeviceType'])
    inside_list.append(response1['Reservations'][0]['Instances'][0]['State']['Name'])
    outside_list.append(inside_list)

print(outside_list)    

# Writing the CSV file
header = ['InstanceId', 'InstanceType', 'PrivateIpAddress', 'RootDeviceType', 'State']
data1 = pd.DataFrame(outside_list, columns=header)
data1.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\instance-status.csv", index=False)

# Reading the latest written file from above
df1 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\instance-status.csv", usecols=['InstanceId', 'State'])
pprint(df1)

# Comparing which instances are running and stopping them
for each1 in range(0,b):
    if df1.iloc[each1]['State'] == 'running':
        response2 = client2.stop_instances(
                        InstanceIds=[
                            df1.iloc[each1]['InstanceId'],
                        ])
    '''else:
        response2 = client2.start_instances(
                        InstanceIds=[
                            df1.iloc[each1]['InstanceId'],
                        ])'''

# Creating another List in Lists to update the latest status
outside_list1 = []
for each2 in range(0,b):
    inside_list1 = []      
    response1 = client2.describe_instances(
                        InstanceIds=[
                            df['instance-id'].values[each2],
                        ],
                        )

    inside_list1.append(response1['Reservations'][0]['Instances'][0]['InstanceId'])
    inside_list1.append(response1['Reservations'][0]['Instances'][0]['InstanceType'])    
    inside_list1.append(response1['Reservations'][0]['Instances'][0]['PrivateIpAddress'])
    inside_list1.append(response1['Reservations'][0]['Instances'][0]['RootDeviceType'])
    inside_list1.append(response1['Reservations'][0]['Instances'][0]['State']['Name'])
    outside_list1.append(inside_list1)

# Writing the CSV file
data1 = pd.DataFrame(outside_list1, columns=header)
data1.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\stopped-instances.csv", index=False)

# Uploading the latest status to S3 bucket
client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\stopped-instances.csv', 'sample88563', 'stopped-instances.csv')
print("Successfully uploaded the file to AWS S3 bucket")