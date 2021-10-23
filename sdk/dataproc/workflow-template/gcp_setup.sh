#!/bin/bash

PROJECT_ID="yygcplearning"
REGION="europe-west1"
ZONE="europe-west1-b"
BUCKET_NAME="gs://dataproc-temp-yt-123456"

KEY_FIL="conf/dataproc-yygcplearning.json"

# activate your service account 
gcloud auth activate-service-account ${PROJECT_ID} --key-file=${KEY_FIL}

# gcp config setup
gcloud components update
gcloud config set project ${PROJECT_ID}

# upload the spark job into the bucket
gsutil cp src/simple_spark_job.py ${BUCKET_NAME}/src
gsutil cp data/input-data.txt ${BUCKET_NAME}/input