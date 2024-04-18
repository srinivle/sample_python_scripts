import samplevolfunc
import boto3
import pandas as pd
import csv as csv
from pprint import pprint
import numpy as np
import os
session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')
client2 = session.client('ec2')

df4 = pd.read_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\sanpshot-status2.csv", usecols=['SnapshotId', 'StartTime', 'Snapshot Days Difference'])

for each in range(0,len(df4['Snapshot Days Difference'])):
    if df4['Snapshot Days Difference'].values[each] > 5:
        response = client2.delete_snapshot(
            SnapshotId=df4['SnapshotId'].values[each],)
pprint("Successfully deleted the snapshots of volumes")
