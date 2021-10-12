# GCP Dataproc + Gitlab + Terraform

## Provisining with Terraform
1. create GCS buckets
- yygcplearning-spark-project

2. create a dataproc cluster
- my-nice-dataproc-cluster

3. create a dataproc job
- pyspark

## Configuration in GCS Buckets (data upload)
- gs://yygcplearning-spark-project/gitlab/test-input-data/
- gs://yygcplearning-spark-project/gitlab/src/

## Submission Dataproc jobs

## run a simple spark without input and output
```bash
BUCKET_NAME="yygcplearning-spark-project"

gcloud dataproc jobs submit pyspark spark_test_run.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/spark_test_run.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \

```
## run a simple spark with input and output
```bash
gcloud dataproc jobs submit pyspark word_count.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \
    -- gs://${BUCKET_NAME}/gitlab/test-input-data/rose.txt gs://${BUCKET_NAME}/output/

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/word_count.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \
    -- gs://${BUCKET_NAME}/gitlab/test-input-data/rose.txt gs://${BUCKET_NAME}/output/
```
## run a simple spark which uses GCS bucket
```bash
BUCKET_NAME="yygcplearning-spark-project"

gcloud dataproc jobs submit pyspark prep_engine.py \
      --cluster=my-nice-dataproc-cluster \
      --region=europe-west3 \

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/spark/prep_engine.py \
      --cluster=my-nice-dataproc-cluster \
      --region=europe-west3 \
```