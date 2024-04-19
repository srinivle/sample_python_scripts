import boto3
import pandas as pd
from pprint import pprint
from io import StringIO

#Opening the Boto3 Session.
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')

df = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\volume-status.csv", usecols=['VolumeId', 'State', 'TagValue'])
b = len(df)

for each in range(0,b):
    if df['State'].values[each] == 'available' and df['TagValue'].values[each] == 'Prod':
        response = client2.delete_volume(
            VolumeId=df['VolumeId'].values[each],)

pprint(" Successfully deleted the Volumes which has TagValue as 'Prod' ")        


