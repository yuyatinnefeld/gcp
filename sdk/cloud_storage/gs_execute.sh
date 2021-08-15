#!/bin/bash

OBJECT_NAME="sample123"
LOCAL_FILE_PATH="data/ratings.csv"
DESTINATION_BUCKET="sample123"
STORAGE_CLASS="Standard"
REGION="europe-west3"
BUCKET_NAME=$DEVSHELL_PROJECT_ID-$OBJECT_NAME


gsutil mb -p $DEVSHELL_PROJECT_ID \
    -c ${STORAGE_CLASS} \
    -l ${REGION} \
    gs://$BUCKET_NAME/


gsutil cp -r $LOCAL_FILE_PATH/* gs://$DESTINATION_BUCKET