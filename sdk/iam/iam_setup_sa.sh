#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
SERVICE_NAME="yuyaiamtest"
SERVICE_ACCOUNT=${SERVICE_NAME}"@"${PROJECT_ID}".iam.gserviceaccount.com"
ROLE_NAME="roles/owner"
BUCKET_NAME="yuyabucket_12345"

## Create Service Account ##
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud iam service-accounts list

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud alpha iam service-accounts create ${SERVICE_NAME}  --display-name="yu test display name"

## Update Service Account ##
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud alpha iam service-accounts describe ${SERVICE_ACCOUNT}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud alpha iam service-accounts enable  ${SERVICE_ACCOUNT}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
  gcloud projects add-iam-policy-binding ${PROJECT_ID}  \
    --member="serviceAccount:"${SERVICE_ACCOUNT} \
    --role=${ROLE_NAME}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectAdmin \
  gs://${BUCKET_NAME}

