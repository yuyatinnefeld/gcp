# GCP Data Processing Project

## Tech stacks
- GCS
- Dataproc
- Pyspark

## Data flow Process
- the row data "gs://${BUCKET_NAME_DATA}/input/rose.txt" is a text data.
- this text data will be counted through the Pyspark job
- this pyspark file is stored in the GCS bucket
- a Dataproc cluster executes this job
- the output data will be stored into the "gs://${BUCKET_NAME_DATA}/output/"

## GCS Buckets setup
1. create a GCS bucket
```bash
REGION="europe-west3"
STORAGE_CLASS="Standard"

BUCKET_NAME_GIT="$DEVSHELL_PROJECT_ID-processing-git"
BUCKET_NAME_DATA="$DEVSHELL_PROJECT_ID-processing-data"

gsutil mb -p $DEVSHELL_PROJECT_ID -c ${STORAGE_CLASS} -l ${REGION} -b on gs://${BUCKET_NAME_GIT}
gsutil mb -p $DEVSHELL_PROJECT_ID -c ${STORAGE_CLASS} -l ${REGION} -b on gs://${BUCKET_NAME_DATA}
gsutil cp gs://pub/shakespeare/rose.txt \ gs://${BUCKET_NAME_DATA}/input/rose.txt
```

## Create a Gitlab Project

- ex. gcp-dataprocessing
1. create the following folders / files
    - conf
    - pyspark/processing1.py
    - .gitlab-ci.yml

processing1.py
```python
#!/usr/bin/env python

import pyspark
import sys

print("processing 1")

if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]

sc = pyspark.SparkContext()
lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1 + count2)
wordCounts.saveAsTextFile(sys.argv[2])
```

.gitlab-ci.yml
```yaml
deploy-git-to-gcs:
  stage: deploy
  image: google/cloud-sdk
  before_script:
    - echo ""
  script:
    - gcloud auth activate-service-account --key-file ${GCP_SERVICE_KEY}
    - gcloud config list
    - gcloud config set project ${GCP_PROJECT_ID}
    - gsutil -m cp -r * gs://${GCP_DATA_BUCKET}/
  when: manual
```

2. create the gitlab variables

- GCP_DATA_BUCKET: variable
- GCP_PROJECT_ID: variable
- GCP_SERVICE_KEY: file

3. run the cicd pipeline 

4. verify the objects in the GCS bucket


## Dataproc Cluster
1. create a cluster

```bash
PROJECT_ID=$(gcloud config get-value project)
CLUSTER_NAME="pyspark-cluster"
REGION="europe-west3"
WORKERS=3

gcloud config set project ${PROJECT_ID}
gcloud dataproc clusters create ${CLUSTER_NAME} --region=${REGION}
```


2. create a pyspark job and using the new cluster
```bash
REGION="europe-west3"
CLUSTER_NAME="pyspark-cluster"
BUCKET_NAME_GIT="$PROJECT_ID-processing-git"
BUCKET_NAME_DATA="$PROJECT_ID-processing-data"
JOB_NAME="pyspark-word-count"

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME_GIT}/pyspark/processing1.py \
    --cluster=${CLUSTER_NAME} \
    --id ${JOB_NAME} \
    --region=${REGION} \
    -- gs://${BUCKET_NAME_DATA}/input/ gs://${BUCKET_NAME_DATA}/output/
```

- selected the pyspark file   (gs://yygcplearning-processing-git/pyspark/processing1.py)

## Check the result

```bash
gsutil cat gs://${BUCKET_NAME_DATA}/output/*
```

