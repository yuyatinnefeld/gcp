#!/bin/bash

REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
STORAGE_CLASS="Standard"
BUCKET_NAME="yuyabucket_12345"
DATASET="dataset_20210615"
TABLE_NAME1="ratings"
TABLE_NAME2="movies"
EXPIRATION=36000

## create a dataset
bq mk \
    --location=${REGION} \
    --project_id=${PROJECT_ID} \
    ${DATASET}

## create tables
bq mk \
    --table \
    --expiration ${EXPIRATION} \
    --label organization:development \
    ${DATASET}.${TABLE_NAME1} \


bq mk \
    --table \
    --expiration ${EXPIRATION} \
    --description "table XXXXX for YYYYY" \
    --label organization:development \
    ${DATASET}.${TABLE_NAME1} \
    userId:INT64,movieId:INT64,rating:FLOAT,timestamp:INT64

bq mk \
    --table \
    --expiration ${EXPIRATION} \
    --description "table XXXXX for YYYYY" \
    --label organization:development \
    ${DATASET}.${TABLE_NAME2} \
    movieId:INT64,title:STRING,genres:STRING


bq show ${DATASET}.${TABLE_NAME1}

bq show ${DATASET}.${TABLE_NAME2}