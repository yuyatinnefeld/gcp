#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
PASSWORD="password123"
CPU_NUM=2
MEMORY_SIZE="4GiB"
DBTYPE="POSTGRES_9_6"
DBNAME="prod-db-lowercase"
BUCKET_NAME="yuyabucket_12345"
FILE_NAME_1="ratings.csv"
TABLE_NAME="new-table"


docker exec -it gcloud-config \
gcloud sql instances create ${DBNAME}  \
--database-version=${DBTYPE} --cpu=${CPU_NUM} --memory=${MEMORY_SIZE}  \
--zone=${ZONE} --root-password=${PASSWORD}

docker exec -it gcloud-config \
gcloud sql instances describe ${DBNAME}

#create table
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
gcloud sql \
  import csv ${DBNAME} \
  gs://${BUCKET_NAME}/${FILE_NAME_1} \
  --database=${DBNAME}  --table=${TABLE_NAME}

#import from gs
gcloud sql import sql [INSTANCE_NAME] gs://[BUCKET_NAME]/[IMPORT_FILE_NAME] \
                            --database=[DATABASE_NAME]