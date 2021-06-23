#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
STORAGE_CLASS="Standard"
BUCKET_NAME="yuyabucket_12345"
DATASET="dataset_20210615"
TABLE_NAME1="ratings"
TABLE_NAME2="movies"

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq mk \
    --table \
    --expiration 36000 \
    --description "table XXXXX for YYYYY" \
    --label organization:development \
    ${DATASET}.${TABLE_NAME1} \
    userId:INT64,movieId:INT64,rating:FLOAT,timestamp:INT64

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq mk \
    --table \
    --expiration 36000 \
    --description "table XXXXX for YYYYY" \
    --label organization:development \
    ${DATASET}.${TABLE_NAME2} \
    movieId:INT64,title:STRING,genres:STRING


docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq show ${DATASET}.${TABLE_NAME1}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq show ${DATASET}.${TABLE_NAME2}