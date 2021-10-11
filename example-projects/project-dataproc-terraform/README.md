# GCP Dataproc + Gitlab + Terraform

## Terraform Setup
1. create GCS buckets
- yygcplearning-spark-project

2. create a dataproc cluster
- my-nice-dataproc-cluster

3. create a dataproc job
- pyspark


## Dataproc job Submission

## run a simple spark without input and output
```bash
BUCKET_NAME="yygcplearning-spark-project"

gcloud dataproc jobs submit pyspark spark-test-run.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/spark-test-run.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \

```
## run a simple spark with input and output
```bash
gcloud dataproc jobs submit pyspark word-count.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \
    -- gs://${BUCKET_NAME}/gitlab/test-input-data/rose.txt gs://${BUCKET_NAME}/output/

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/word-count.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \
    -- gs://${BUCKET_NAME}/gitlab/test-input-data/rose.txt gs://${BUCKET_NAME}/output/
```


## run a simple spark with 2 input args (json)
```bash
BUCKET_NAME="yygcplearning-spark-project"
BUCKET_INPUT_DATA="yygcplearning-spark-project/gitlab/test-input-data"

gcloud dataproc jobs submit pyspark gs://${BUCKET_NAME}/gitlab/src/simple-spark-join.py \
    --cluster=my-nice-dataproc-cluster \
    --region=europe-west3 \
    -- gs://${BUCKET_INPUT_DATA}/customer.json gs://${BUCKET_INPUT_DATA}/product.json
```