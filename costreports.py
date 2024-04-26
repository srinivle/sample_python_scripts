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
client3 = session.client('ce')

response = client3.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-04-01',
        'End': '2024-04-25'
    },
    Granularity='MONTHLY',
    Filter = { "Dimensions": { "Key": "LINKED_ACCOUNT", "MatchOptions": [ "EQUALS" ], "Values": [ "058264069674" ] } },
             
    Metrics=[
        'UnblendedCost',
        'BlendedCost',
        'AmortizedCost',
        'NetAmortizedCost',
        'NetUnblendedCost',
    ],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
    ],
    #NextPageToken='string'
    
)

p = []
p.append(response['ResultsByTime'][0]['Groups'][0]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][1]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][2]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][3]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][4]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][5]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][6]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][7]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][8]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][9]['Keys'][0])
p.append(response['ResultsByTime'][0]['Groups'][10]['Keys'][0])

pprint(p)
a = []
#a.append(p)
for each in range(0,11):
    b = []
    b.append(response['ResultsByTime'][0]['Groups'][each]['Metrics']['AmortizedCost']['Amount'])
    b.append(response['ResultsByTime'][0]['Groups'][each]['Metrics']['NetAmortizedCost']['Amount'])
    b.append(response['ResultsByTime'][0]['Groups'][each]['Metrics']['BlendedCost']['Amount'])
    b.append(response['ResultsByTime'][0]['Groups'][each]['Metrics']['UnblendedCost']['Amount'])
    b.append(response['ResultsByTime'][0]['Groups'][each]['Metrics']['NetUnblendedCost']['Amount'])
    a.append(b)

pprint(a)

header = ['AmortizedCost(Amounts in USD)', 'NetAmortizedCost(Amounts in USD)', 'BlendedCost(Amounts in USD)', 'UnblendedCost(Amounts in USD)', 'NetUnblendedCost(Amounts in USD)']
data = pd.DataFrame(a, columns=header)
new_col = pd.DataFrame(p)
data.insert(0,'List of Services', new_col, allow_duplicates=True)
data.to_csv(r"C:\Users\pleel\OneDrive\Downloads\samplecodes-virtusa\python-codes\aws-services-costreport.csv", index=False)
client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\aws-services-costreport.csv', 'sample88563', 'aws-services-costreport.csv')
print("Successfully uploaded the 'AWS Services Cost Usage Report' file to AWS S3 bucket")


