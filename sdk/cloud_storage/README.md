# Cloud Storage
Info: https://cloud.google.com/storage/docs/moving-buckets

### define ENV variables
```bash
PROJECT=xxxxx
REGION=xxxxx
ZONE=xxxxx
PROJECT_ID=xxxxx
STORAGE_CLASS=xxxx
BUCKET_NAME=xxxx
```

## create a bucket
```bash
gsutil mb -p ${PROJECT} -c ${STORAGE_CLASS} -l ${REGION} -b on gs://${BUCKET_NAME}
```
## check buckets
```bash
gsutil ls
```

##upload cloud file into the gs bucket
```bash
gsutil cp -r gs://${SOURCE_BUCKET}/* gs://${DESTINATION_BUCKET}
```

## upload local file into the gs bucket
```bash
gsutil cp ${LOCAL_FILE_PATH}/* gs://${DESTINATION_BUCKET}
```

## download the file from gs
```bash
gsutil cp gs://{BUCKET_NAME}/{FILE_NAME} {LOCAL_FILE_PATH}
```

## remove bucket / file
```bash
gsutil rm -r gs://{BUCKET_NAME}
```