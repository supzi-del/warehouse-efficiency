import boto3
import pandas as pd
from io import StringIO

# Initialize S3 client
s3 = boto3.client('s3')

# Define your bucket and file name
bucket_name = 'warehouse-efficiency-data'
file_key = 'combined_batches.csv'

# Download file object
obj = s3.get_object(Bucket=bucket_name, Key=file_key)

# Read content into a pandas DataFrame
data = obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(data))

# Show preview
print("Preview of Ingested Batch:")
print(df.head())
