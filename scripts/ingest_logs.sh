#!/bin/bash

# Check if a date argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 YYYY-MM-DD"
    exit 1
fi

# Extract year, month, and day from the provided date
DATE="$1"
YEAR=$(date -d "$DATE" '+%Y')
MONTH=$(date -d "$DATE" '+%m')
DAY=$(date -d "$DATE" '+%d')

# Define HDFS directories
HDFS_LOGS_DIR="/raw/logs/$YEAR/$MONTH/$DAY/"
HDFS_METADATA_DIR="/raw/metadata/$YEAR/$MONTH/$DAY/"

# Define local directories where the data is stored
LOCAL_LOGS_DIR="./raw_data/$DATE/logs/"
LOCAL_METADATA_DIR="./raw_data/$DATE/metadata/"

# Create directories in HDFS
hdfs dfs -mkdir -p "$HDFS_LOGS_DIR"
hdfs dfs -mkdir -p "$HDFS_METADATA_DIR"

# Move log files into HDFS
hdfs dfs -put "$LOCAL_LOGS_DIR"*.csv "$HDFS_LOGS_DIR"
hdfs dfs -put "$LOCAL_LOGS_DIR"*.json "$HDFS_LOGS_DIR"

# Move metadata files into HDFS
hdfs dfs -put "$LOCAL_METADATA_DIR"*.csv "$HDFS_METADATA_DIR"
hdfs dfs -put "$LOCAL_METADATA_DIR"*.json "$HDFS_METADATA_DIR"

echo "Data ingestion complete for date: $DATE"
