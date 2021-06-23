#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"

docker exec -it gcloud-config gcloud auth login

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud projects create ${PROJECT_ID} --name=${PROJECT} --labels=type=learn

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud config set project ${PROJECT_ID}

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud config list

