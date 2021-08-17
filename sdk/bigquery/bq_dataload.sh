#!/bin/bash

REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
BUCKET_NAME="yuyabucket_12345"
DATASET="dataset_20210615"
TABLE_NAME1="ratings"
TABLE_NAME2="movies"
FORMAT_CSV="CSV"
FORMAT_AVRO="AVRO"

FILE_NAME_1="ratings.csv"
FILE_NAME_2="movies.csv"
ROWS=1

# load CSV from cloud storage 
bq load \
    --source_format=${FORMAT_CSV} \
    --skip_leading_rows ${ROWS} \
    --autodetect \
    ${DATASET}.${TABLE_NAME1} \
    gs://${BUCKET_NAME}/${FILE_NAME_1}


bq load \
    --source_format=${FORMAT_CSV} \
    --skip_leading_rows ${ROWS} \
    --autodetect \
    ${DATASET}.${TABLE_NAME2} \
    gs://${BUCKET_NAME}/${FILE_NAME_2}

# load AVRO from cloud storage 
bq load \
    --source_format=${FORMAT_AVRO} \
    ${DATASET}.${TABLE_NAME1} \
    gs://${BUCKET_NAME}/${FILE_NAME_1}