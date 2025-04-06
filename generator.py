import pandas as pd
import random
import os
import glob

def generate_batch(batch_id, num_records=20):
    bins = ['A1', 'A2', 'B1', 'B2', 'C3', 'D4', 'E5']
    robots = ['R1', 'R2', 'R3']
    records = []

    for _ in range(num_records):
        start_bin = random.choice(bins)
        end_bin = random.choice(bins)
        robot = random.choice(robots)
        pick_time = random.randint(60, 240)  # in seconds
        records.append({
            'batch_id': batch_id,
            'robot_id': robot,
            'start_bin': start_bin,
            'end_bin': end_bin,
            'expected_time_sec': 120,
            'actual_time_sec': pick_time
        })

    df = pd.DataFrame(records)
    os.makedirs('data', exist_ok=True)
    df.to_csv(f'data/batch_{batch_id}.csv', index=False)
    print(f"Generated batch_{batch_id}.csv")


# Generate multiple batches
for i in range(1, 4):
    generate_batch(str(i).zfill(3))


# Combine all batch files into one for Tableau
def combine_batches():
    batch_files = glob.glob("data/batch_*.csv")
    all_data = pd.concat((pd.read_csv(f) for f in batch_files), ignore_index=True)
    combined_path = "data/combined_batches.csv"
    all_data.to_csv(combined_path, index=False)
    print(f"Combined all batches into {combined_path}")

combine_batches()
