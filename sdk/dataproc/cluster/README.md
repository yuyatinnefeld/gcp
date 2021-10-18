# Cluster Configuration

## Auto Scaling

The Dataproc AutoscalingPolicies API provides a mechanism for automating cluster resource management and enables cluster worker VM autoscaling. 

## Case for auto scaling

- for the cluster which stores data in external services (i.g. Cloud Storage or BigQuery)
- for the cluster which proccess many jobs
- to scale up a single-job cluster

## Step to use auto scaling

- step1: create autoscaling policies
- step2: create a new cluster with autoscaling policies or update the existing cluster with the autoscaling policies

```bash
POLICY_NAME="my-demo-autoscaling-policies"
FILE_NAME="my-autoscaling-policies.yaml"
REGION="europe-west3"
gcloud dataproc autoscaling-policies import ${POLICY_NAME} \
    --source=${FILE_NAME} \
    --region=${REGION}
```

```yaml
workerConfig:
  minInstances: 2
  maxInstances: 10
  weight: 1
secondaryWorkerConfig:
  minInstances: 0
  maxInstances: 100
  weight: 1
basicAlgorithm:
  cooldownPeriod: 2m
  yarnConfig:
    scaleUpFactor: 0.05
    scaleDownFactor: 1.0
    scaleUpMinWorkerFraction: 0.0
    scaleDownMinWorkerFraction: 0.0
    gracefulDecommissionTimeout: 1h
```

```bash
# create a new cluster with autoscaling policies

CLUSTER_NAME="hey-demo-cluster"
gcloud dataproc clusters create ${CLUSTER_NAME} \
    --autoscaling-policy=${POLICY_NAME} \
    --region=${REGION} \
    --num-workers 2

# update an existing cluster with the autoscaling policies

gcloud dataproc clusters update ${CLUSTER_NAME} \
    --autoscaling-policy=${POLICY_NAME} \
    --region=${REGION}
```

## EFM (Enhanced Flexibility Mode)

- primary worker shuffel
- only spark job
- suitable for preemptible workers or scaling second worker group


## Create a cluster with the service account
```bash
gcloud dataproc clusters create ${CLUSTER_NAME} \
    --region=${REGION} \
    --service-account=service-account-name@project-id.iam.gserviceaccount.com \
    --scopes=scope[, ...]
```

## Dataproc buckets
- By default Dataproc creates 2 buckets
- staging bucket: used to stage cluster job dependencies, job driver output, and cluster config files
- temp bucket: used to store ephemeral cluster and jobs data (i.e. Spark and MapReduce history files)
- by default, temp bucket has a TTL of 90 days.

create 
```bash
gcloud dataproc clusters create ${CLUSTER_NAME} \
    --region=${REGION} \
    --bucket=${STAGING_BUCKET_NAME} \
    --temp-bucket=${TEMP_BUCKET_NAME}

# see the detail about the cluster
gcloud dataproc clusters describe ${CLUSTER_NAME} \
    --region=${REGION}
```