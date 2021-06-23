#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
BUCKET_NAME="yuyabucket_12345"
DATASET="dataset_20210615"
TABLE_NAME1="ratings"
TABLE_NAME2="movies"
FORMAT="CSV"
FILE_NAME_1="ratings.csv"
FILE_NAME_2="movies.csv"


docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq load \
    --source_format=${FORMAT} \
    --skip_leading_rows 1 \
    --autodetect \
    ${DATASET}.${TABLE_NAME1} \
    gs://${BUCKET_NAME}/${FILE_NAME_1}


docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq load \
    --source_format=${FORMAT} \
    --skip_leading_rows 1 \
    --autodetect \
    ${DATASET}.${TABLE_NAME2} \
    gs://${BUCKET_NAME}/${FILE_NAME_2}