#!/bin/bash

TEMPLATE_ID="my_workflow_template_id_1234"
REGION="europe-west1"
ZONE="europe-west1-b"
STEP_ID1="simple-pyspark1"
STEP_ID2="simple-pyspark2"
BUCKET_NAME="gs://dataproc-temp-yt-123456"
SPARK_JOB_1=${BUCKET_NAME}"/src/simple_spark_job1.py"
SPARK_JOB_2=${BUCKET_NAME}"/src/simple_spark_job2.py"

#job1 without arg
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_1} \
  --step-id ${STEP_ID1} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION}


#job2 read a GSC bucket file
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_2} \
  --step-id ${STEP_ID2} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION}
  
#job3 with args
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_2} \
  --step-id ${STEP_ID2} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION} \
  -- ${BUCKET_NAME}/input/input-data.txt \
    ${BUCKET_NAME}/output/