#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
STORAGE_CLASS="Standard"
BUCKET_NAME="yuyabucket_spark_12345"
LOCAL_FILE_PATH="data/ratings.csv"
DESTINATION_BUCKET="yuyabucket_12345"
WORKER_TYPE="n1-standard-8"
WORKER_NUM=3
CLUSTER_NAME="spcluster-today-is-a-good-day-20210615"
IMAGE="1.5-debian"

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gsutil mb -p ${PROJECT_ID} -c ${STORAGE_CLASS} -l ${REGION} -b on gs://${BUCKET_NAME}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud services enable compute.googleapis.com \
  dataproc.googleapis.com \
  bigquerystorage.googleapis.com

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud dataproc clusters create ${CLUSTER_NAME} \
  --project=${PROJECT_ID} \
  --region=${REGION} \
  --image-version ${IMAGE} \
  --optional-components=ANACONDA
  --single-node

 gcloud beta dataproc clusters create ${CLUSTER_NAME} \
     --project=${PROJECT_ID} \
     --region=${REGION} \
     --worker-machine-type n1-standard-8 \
     --single-node
     --image-version 1.5-debian \
     --initialization-actions gs://dataproc-initialization-actions/python/pip-install.sh \
     --metadata 'PIP_PACKAGES=google-cloud-storage' \
     --optional-components=ANACONDA \
     --enable-component-gateway


gcloud dataproc jobs submit pyspark --cluster ${CLUSTER_NAME} \
    --region=${REGION} \
    --jars gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
    --driver-log-levels root=FATAL \
    counts_by_subreddit.py