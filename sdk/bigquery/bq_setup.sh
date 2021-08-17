#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
DATASET="dataset_20210615"
EXPIRATION=36000
bq mk \
    --dataset \
    --default_table_expiration ${EXPIRATION} \
    --description "dataset XXXXX for YYYYY" \
    ${DATASET}

