#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
STORAGE_CLASS="Standard"
BUCKET_NAME="yuyabucket_12345"
LOCAL_FILE_PATH="data/ratings.csv"
DESTINATION_BUCKET="yuyabucket_12345"

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
gsutil mb -p ${PROJECT_ID} -c ${STORAGE_CLASS} -l ${REGION} -b on gs://${BUCKET_NAME}


docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
gsutil cp -r ${LOCAL_FILE_PATH}/* gs://${DESTINATION_BUCKET}