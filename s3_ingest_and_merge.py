import boto3
import pandas as pd
import os
from io import StringIO

BUCKET = 'warehouse-efficiency-data'
LOCAL_MASTER = 'combined_batches.csv'
PROCESSED_LOG = 'processed_files.txt'

s3 = boto3.client('s3')

# Load processed files
if os.path.exists(PROCESSED_LOG):
    with open(PROCESSED_LOG, 'r') as f:
        processed = set(f.read().splitlines())
else:
    processed = set()

# Get list of batch files in S3
response = s3.list_objects_v2(Bucket=BUCKET)
batch_files = [obj['Key'] for obj in response['Contents'] if obj['Key'].startswith('batch_')]

# Load local master if it exists
if os.path.exists(LOCAL_MASTER):
    master_df = pd.read_csv(LOCAL_MASTER)
else:
    master_df = pd.DataFrame()

# Process each new batch file
for key in batch_files:
    if key in processed:
        continue

    print(f"📥 Ingesting: {key}")
    obj = s3.get_object(Bucket=BUCKET, Key=key)
    content = obj['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(content))

    master_df = pd.concat([master_df, df], ignore_index=True)
    processed.add(key)

# Save updated master file
master_df.to_csv(LOCAL_MASTER, index=False)

# Save processed file log
with open(PROCESSED_LOG, 'w') as f:
    f.write('\n'.join(processed))

print(f"Updated {LOCAL_MASTER} with {len(processed)} batches.")
