# Dataproc

## create a cluster
```bash
PROJECT_ID=$(gcloud config get-value project)
CLUSTER_NAME="yt-cluster"
REGION="europe-west3"
WORKERS=5

# connect to your GCP project
gcloud config set project ${PROJECT_ID}

# create dataproc clusters
# GCE instances + cloud storage instances are created
gcloud dataproc clusters create ${CLUSTER_NAME} --region=${REGION}
```

## submit a demo job
```bash
gcloud dataproc jobs submit spark --cluster example-yt-cluster \
    --region=region \
    --class org.apache.spark.examples.SparkPi \
    --jars file:///usr/lib/spark/examples/jars/spark-examples.jar -- 1000
```

## update a cluster (increase workers)

```bash
gcloud dataproc clusters update ${CLUSTER_NAME} \
    --region=region \
    --num-workers ${WORKERS}
```

## run spark job run with a custom jar file

1. write a custom jar file

1.2 create scala object
```scala
package gcp

import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

object WordCount {
def main(args: Array[String]) {
    if (args.length != 2) {
        throw new IllegalArgumentException(
        "Exactly 2 arguments are required: <inputPath> <outputPath>")
    }

    val inputPath = args(0)
    val outputPath = args(1)

    val sc = new SparkContext(new SparkConf().setAppName("Word Count"))
    val lines = sc.textFile(inputPath)
    val words = lines.flatMap(line => line.split(" "))
    val wordCounts = words.map(word => (word, 1)).reduceByKey(_ + _)
    wordCounts.saveAsTextFile(outputPath)
    }
}
```
1.3 build package
```bash
sbt clean package
```

2. store the package into GCS bucket
```bash
gsutil cp target/scala-2.12/my-app_2.12-1.0.jar \
gs://${BUCKET_NAME}/my-app_2.12-1.0.jar
```

3. select this jar file and class by the setting up "dataproc jobs submit"

```bash
gcloud dataproc jobs submit spark --cluster example-yt-cluster \
    --region=region \
    --class org.apache.spark.xxx.XXX \
    --jars gs://xxxx-bucketusr/my-app_2.12-1.0.jar -- 1000
```

## run spark job in the dataproc Web UI
1. ssh connect to a cluster instance (GCE) 
```bash
PROJECT_ID=$(gcloud config get-value project)
CLUSTER_NAME="yt-cluster"
GCE_INSTANCE="yt-cluster-m"
ZONE="europe-west3"

# connect to your GCP project
gcloud config set project ${PROJECT_ID}

# ssh connect
gcloud beta compute ssh --zone ${ZONE} ${GCE_INSTANCE} --project ${PROJECT_ID}

# start spark session
spark-shell

# read a file from the GCS bucket
val text_file = sc.textFile("gs://pub/shakespeare/rose.txt")

# run a wordcoutn mapreduce
val wordCounts = text_file.flatMap(line => line.split(" ")).map(word =>
(word, 1)).reduceByKey((a, b) => a + b)

# check the result
wordCounts.show()

# save the result
wordCounts.collect

# store the result into the GCS bucket
wordCounts.saveAsTextFile("gs://yygcplearning-ds/wordcounts-out/")

exit

# check the outputs in the bucket
gsutil ls gs://yygcplearning-ds/wordcounts-out/

# show the result
gsutil cat gs://yygcplearning-ds/wordcounts-out/part-00000

# delete the data
gsutil rm -r gs://yygcplearning-ds/wordcounts*
```

## delete a cluster
```bash
gcloud dataproc clusters delete ${CLUSTER_NAME} \
    --region=region

# delete GCS bucket instances
gsutil rm -r gs://dataproc-staging*
gsutil rm -r gs://dataproc-temp*
```



## run the spark wordcount app
```bash
gcloud dataproc jobs submit spark \
--cluster=${CLUSTER} \
--class=gcp.CloudStorageWordCount \
--jars=gs://${BUCKET_NAME}/scala/my-app_2.12-1.0.jar \
--region=${REGION} \
-- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```

read the result from cloud storage bucket
```bash
gsutil cat gs://${BUCKET_NAME}/output/*
```

another source: Info: https://codelabs.developers.google.com/codelabs/pyspark-bigquery#6
