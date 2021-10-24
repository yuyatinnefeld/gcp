#!/bin/bash

TEMPLATE_ID="my_workflow_template_id_1234"
REGION="europe-west1"
ZONE="europe-west1-b"
STEP_ID1="simple-pyspark1"
STEP_ID2="simple-pyspark2"
STEP_ID3="prediction-pyspark"
BUCKET_NAME="gs://dataproc-temp-yt-123456"
SPARK_JOB_1=${BUCKET_NAME}"/src/simple_spark_job1.py"
SPARK_JOB_2=${BUCKET_NAME}"/src/simple_spark_job2.py"
SPARK_JOB_3=${BUCKET_NAME}"/src/pyspark_sa.py"


# store the spark scripts to GCS
gsutil cp src/simple_spark_job1.py gs://${BUCKET}/src/simple_spark_job1.py
gsutil cp src/simple_spark_job2.py gs://${BUCKET}/src/simple_spark_job2.py
gsutil cp src/pyspark_sa.py gs://${BUCKET}/src/pyspark_sa.py


# job1 - run simple spark script without arg
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_1} \
  --step-id ${STEP_ID1} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION}

# job2 - run simple spark script without arg
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_2} \
  --step-id ${STEP_ID2} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION}
  

# job3 - run ML spark script with args
gcloud dataproc workflow-templates add-job pyspark \
  ${SPARK_JOB_3} \
  --step-id ${STEP_ID3} \
  --workflow-template ${TEMPLATE_ID} \
  --region ${REGION} \
  -- ${BUCKET_NAME}/input/ \
   ${BUCKET_NAME}/output \
   ${BUCKET_NAME}/model


# delete job
gcloud dataproc workflow-templates remove-job ${TEMPLATE_ID} --region ${REGION} --step-id=${STEP_ID3}
