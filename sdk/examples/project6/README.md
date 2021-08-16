# GCP Project 6 - Hosting a static website using HTTP

## About
- Upload Static Website in the Cloud Storage
- how to serve content over HTTP by GCP

## Info
- https://codelabs.developers.google.com/codelabs/cloud-webapp-hosting-gcs#2
- https://cloud.google.com/storage/docs/hosting-static-website#storage-create-bucket-gsutil

## Create Cloud storage backet
- Storage access control model: set object-level and bucket-level permission


```bash
STORAGE_CLASS="Standard"
REGION="europe-west3"
BUCKET_NAME="yuyatinnefeld-profileweb"


gsutil mb -p $DEVSHELL_PROJECT_ID \
    -c ${STORAGE_CLASS} \
    -l ${REGION} \
    -b on gs://$BUCKET_NAME/

gsutil cp profile gs://$BUCKET_NAME
gsutil iam ch allUsers:objectViewer gs://$BUCKET_NAME
gsutil web set -m index.html -e 404.html gs://$BUCKET_NAME
```



