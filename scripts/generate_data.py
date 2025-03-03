import os
import random
import pandas as pd
from datetime import datetime, timedelta

# Define paths
RAW_DATA_DIR = "../raw_data"
LOGS_SUBDIR = "logs"
METADATA_SUBDIR = "metadata"

# Ensure raw_data folder exists
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Define possible values
actions = ["play", "pause", "skip", "forward"]
devices = ["mobile", "desktop", "tablet"]
regions = ["US", "EU", "APAC"]
content_ids = list(range(1000, 1011))
user_ids = list(range(100, 201))

# Generate user logs for 7 days
for i in range(7):
    date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
    logs_path = os.path.join(RAW_DATA_DIR, date, LOGS_SUBDIR)
    metadata_path = os.path.join(RAW_DATA_DIR, date, METADATA_SUBDIR)
    os.makedirs(logs_path, exist_ok=True)
    os.makedirs(metadata_path, exist_ok=True)

    # Generate user logs
    logs = []
    for _ in range(random.randint(20, 30)):  # 20-30 entries per day
        logs.append([
            random.choice(user_ids),
            random.choice(content_ids),
            random.choice(actions),
            datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            random.choice(devices),
            random.choice(regions),
            f"session_{random.randint(1000, 9999)}"
        ])
    
    # Save logs as CSV
    log_df = pd.DataFrame(logs, columns=["user_id", "content_id", "action", "timestamp", "device", "region", "session_id"])
    log_df.to_csv(os.path.join(logs_path, "user_logs.csv"), index=False)

# Generate content metadata (once, since it’s static)
metadata = []
for content_id in content_ids:
    metadata.append([
        content_id,
        f"Content {content_id}",
        random.choice(["Pop", "Rock", "Podcast", "News", "Jazz"]),
        random.randint(180, 600),  # Length in seconds
        f"Artist {random.randint(1, 10)}"
    ])

# Save metadata as CSV
metadata_df = pd.DataFrame(metadata, columns=["content_id", "title", "category", "length", "artist"])
metadata_df.to_csv(os.path.join(metadata_path, "content_metadata.csv"), index=False)

print(f"Saving logs to: {os.path.abspath(os.path.join(logs_path, 'user_logs.csv'))}")
print(f"Saving metadata to: {os.path.abspath(os.path.join(metadata_path, 'content_metadata.csv'))}")
print("Synthetic data generation complete.")
