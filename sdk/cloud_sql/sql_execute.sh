#!/bin/bash

REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="gcptraining-314606"
PASSWORD="password123"
CPU_NUM=2
MEMORY_SIZE="7680MB"
DB_VERSION="MYSQL_8_0"
INSTANCE_NAME="mysql-db-instance"
DB_NAME="mydb123"
BUCKET_NAME="yuyas-test-bucket"
FILE_NAME_1="ratings.csv"
TABLE_NAME="ratings"

#create db instance
docker exec -it gcloud-config \
gcloud sql instances create ${INSTANCE_NAME}  \
--database-version=${DB_VERSION} --cpu=${CPU_NUM} --memory=${MEMORY_SIZE}  \
--zone=${ZONE} --root-password=${PASSWORD}

#check the instance details
docker exec -it gcloud-config \
gcloud sql instances describe ${INSTANCE_NAME}