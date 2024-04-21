import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')
client3 = session.resource('ec2')
waiter = client2.get_waiter('instance_stopped')
p = []
for each in client3.instances.all():
    p.append(each.instance_id)

pprint(p)
header = ['instance-id']
data = pd.DataFrame(p, columns=header)
data.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\list-of-instances.csv", index=False)


client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\list-of-instances.csv', 'sample88563', 'list-of-instances.csv')
print("Successfully uploaded the 'list-of-instances.csv' file to AWS S3 bucket")


# Reading the Object
response = client1.get_object(Bucket='sample88563', Key='list-of-instances.csv')
data = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(data))

# Total number of Objects in CSV File
b = len(df)


# Creating List in Lists to Supply DataFrame
def list_in_lists(b):
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
    return outside_list    

# Writing the CSV file
k = list_in_lists(b)
header = ['InstanceId', 'InstanceType', 'PrivateIpAddress', 'RootDeviceType', 'State']
data1 = pd.DataFrame(k, columns=header)
data1.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\instance-status.csv", index=False)

# Reading the latest written file from above
df1 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\instance-status.csv", usecols=['InstanceId', 'State'])
pprint(df1)

# Stopping those running instances
for each1 in range(0,b):
    if df1.iloc[each1]['State'] == 'running':
        response2 = client2.stop_instances(
                        InstanceIds=[
                            df1.iloc[each1]['InstanceId'],])
        waiter.wait(InstanceIds=[df1.iloc[each1]['InstanceId'],])


# Writing the CSV file
m = list_in_lists(b)
data2 = pd.DataFrame(m, columns=header)
data2.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\stopped-instances.csv", index=False)

# Uploading the latest status to S3 bucket
client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\stopped-instances.csv', 'sample88563', 'stopped-instances.csv')
print("Successfully uploaded the file to AWS S3 bucket")