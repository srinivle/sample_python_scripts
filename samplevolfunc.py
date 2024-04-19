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

# Reading the Object
response = client1.get_object(Bucket='sample88563', Key='list-of-volumes.csv')
data = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(data))
pprint(df)

# Total number of Objects in CSV File
b = len(df)
pprint(b)

def desc_tag_vol(descVol):
    # Describe Tags for List of Volumes

    for each1 in range(0,b):
        response2 = client2.describe_tags(
            Filters=[
            {
                'Name': 'tag:Env',
                'Values': [
                    'Dev',
                ]
            },
        ],
    )
        
    return response2

# Describe Volumes for List of Volumes
def list_in_lists(b):

    outside_list = []
    for each2 in range(0,b):
        inside_list = []             
        response3 = client2.describe_volumes(
                        VolumeIds=[
                        df['volume-id'].values[each2],
                    ],
                )

        #inside_list.append(response3['Volumes'][each2]['Attachments'][0]['InstanceId'])
        inside_list.append(response3['Volumes'][0]['VolumeId'])    
        #inside_list.append(response3['Volumes'][each2]['Attachments'][0]['Device'])
        inside_list.append(response3['Volumes'][0]['VolumeType'])
        inside_list.append(response3['Volumes'][0]['Size'])
        inside_list.append(response3['Volumes'][0]['Tags'][0]['Key'])
        inside_list.append(response3['Volumes'][0]['Tags'][0]['Value'])
        inside_list.append(response3['Volumes'][0]['State'])
        inside_list.append(response3['Volumes'][0]['SnapshotId'])
        
        outside_list.append(inside_list)
    return outside_list

# Writing the CSV file
k = list_in_lists(b)
header = ['VolumeId', 'VolumeType', 'Size', 'TagKey', 'TagValue', 'State', 'SnapshotId']
data1 = pd.DataFrame(k, columns=header)
data1.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\volume-status.csv", index=False)

# Reading the latest written file from above
df1 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\volume-status.csv", usecols=['VolumeId', 'State'])
pprint(df1)
c = len(df1)

# Describe instances using Tags
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


# Creating the Snapshot Status
header = ['SnapshotId', 'StartTime', 'State', 'StorageTier', 'VolumeId', 'VolumeSize', 'TagKey', 'TagValue']
data2 = pd.DataFrame(c, columns=header)
data2.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status.csv", index=False)

# Reading the latest written file from above
df2 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status.csv", usecols=['SnapshotId', 'StartTime'])

# Trimming the StartTime column
ite1 = []
for ite in range(0,len(df2["StartTime"])):
    a = df2["StartTime"].values[ite]
    ite1.append(a.split(' ')[0])

# Updating the StartTime column using Pandas
new_column = pd.Series(ite1, name='StartTime')
data2.update(new_column)
data2.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status1.csv", index=False)
df3 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status1.csv", usecols=['SnapshotId', 'StartTime'])



ite2 = []
for each in range(0, len(df3['StartTime'])):
    d2 = date.today()
    #t2 = d2.strftime("%Y-%m-%d")
    #date1 = datetime.strptime(t2, "%Y-%m-%d")
    date2 = datetime.strptime(ite1[each], "%Y-%m-%d")
    
    # Calculate the difference between the two dates
    diff = relativedelta.relativedelta(date2, d2)
    # Print the number of days between the two dates
    ite2.append(diff.days)


data2.insert(8,"Snapshot Days Difference", ite2, allow_duplicates=True)
data2.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status2.csv", index=False)
df4 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status2.csv", usecols=['SnapshotId', 'StartTime', 'Snapshot Days Difference'])

