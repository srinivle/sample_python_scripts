import boto3
import time
import os
import pandas as pd
import glob
from xlsxwriter import Workbook
from xlsxwriter.workbook import Workbook

session = boto3.Session(profile_name='dev', region_name='us-east-1')
client1 = session.client('s3')

# Collect all the CSV files
path = 'C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\python-codes\\'
all_files = glob.glob(os.path.join(path, "*.csv"))

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("volumeinfo.xlsx", engine="xlsxwriter")

# Collect, Read and Loop all the CSV files and convert them to respective Excel Sheets in a single Excel file 
for f in all_files:
    df = pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()

time.sleep(3)

client1.upload_file('C:\\Users\\pleel\\OneDrive\\Downloads\\samplecodes-virtusa\\volumeinfo.xlsx', 'sample88563', 'volumeinfo.xlsx')
print("Successfully uploaded the file to AWS S3 bucket")
