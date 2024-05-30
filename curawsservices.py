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
client4 = session.client('bcm-data-exports')

now = datetime.now()
now1 = now.strftime("%Y-%m-%d %H:%M:%S")

response = client4.create_export(
    Export={
        "Name": "SampleTestExport",
        "Description": "Example Description",
        "DataQuery": {
            "QueryStatement": "SELECT identity_line_item_id, identity_time_interval, line_item_product_code,line_item_unblended_cost FROM COST_AND_USAGE_REPORT",
            
        },
        "DestinationConfigurations": {
            "S3Destination": {
                "S3Bucket": "sample88563",
                "S3Prefix": "latest",
                "S3Region": "us-east-1",
                "S3OutputConfigurations": {
                    "Overwrite": "OVERWRITE_REPORT",
                    "Format": "TEXT_OR_CSV",
                    "Compression": "GZIP",
                    "OutputType": "CUSTOM"
                }
            }
        },
        "RefreshCadence": {
            "Frequency": "SYNCHRONOUS"
        }
    },
)

pprint(response)
