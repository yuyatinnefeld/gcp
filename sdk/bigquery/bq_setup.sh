#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
DATASET="dataset_20210615"

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq mk \
    --dataset \
    --default_table_expiration 36000 \
    --description "dataset XXXXX for YYYYY" \
    ${DATASET}

