# Workflow Template

- provides a flexible and easy-to-use mechanism for managing and executing workflows
- automates Spark and Hadoop Workloads on GCP
- ideal for automating large batches of dynamic Spark and Hadoop jobs, and for long-running and unattended job execution, such as overnight.
- managed cluster is ephemeral cluster

## Info
- https://garystafford.medium.com/using-the-google-cloud-dataproc-workflowtemplates-api-to-automate-spark-and-hadoop-workloads-on-gcp-95b02f54b5f2

- https://cloud.google.com/dataproc/docs/tutorials/workflow-composer

## Process
- step1: create a workflow template (API or YAML)
- step2: create a managed cluster or select an existing cluster as managed cluster
- step3: add jobs
- step4: instantiate the template


## option 1 - Use WorkflowTemplates API
```bash
TEMPLATE_ID=template_demo_id


# create a template
gcloud dataproc workflow-templates create template-id ${TEMPLATE_ID} \
    --region=region

# set a managed cluster
gcloud dataproc workflow-templates set-managed-cluster \
  $TEMPLATE_ID \
  --region $REGION \
  --zone $ZONE \
  --cluster-name three-node-cluster \
  --master-machine-type n1-standard-4 \
  --master-boot-disk-size 500 \
  --worker-machine-type n1-standard-4 \
  --worker-boot-disk-size 500 \
  --num-workers 2 \
  --image-version 1.3-deb9

# or use an existing cluster
gcloud dataproc workflow-templates set-cluster-selector \
  $TEMPLATE_ID \
  --region $REGION \
  --cluster-labels goog-dataproc-cluster-uuid=$CLUSTER_UUID
```

check the UUID
```bash
CLUSTER_UUID=$(gcloud dataproc clusters describe $CLUSTER_2 \
  --region $REGION \
  | grep 'goog-dataproc-cluster-uuid:' \
  | sed 's/.* //')
echo $CLUSTER_UUID
```

add a job
```bash
export STEP_ID=ibrd-large-pyspark
  
gcloud dataproc workflow-templates add-job pyspark \
  $BUCKET_NAME/international_loans_dataproc.py \
  --step-id $STEP_ID \
  --workflow-template $TEMPLATE_ID \
  --region $REGION \
  -- $BUCKET_NAME \
     ibrd-statement-of-loans-historical-data.csv \
     ibrd-summary-large-python
```


check the template
```bash
gcloud dataproc workflow-templates list --region $REGION

gcloud dataproc workflow-templates describe $TEMPLATE_ID --region $REGION
```


instantiate template
```bash
time gcloud dataproc workflow-templates instantiate \
  $TEMPLATE_ID --region $REGION #--async
```

## option 2 - Use YAML-based Workflow Template

vi my_template.yaml

```yaml
jobs:
- sparkJob:
    jarFileUris:
    - gs://dataproc-demo-bucket/dataprocJavaDemo-1.0-SNAPSHOT.jar
    mainClass: org.example.dataproc.InternationalLoansAppDataprocSmall
  stepId: ibrd-small-spark
- sparkJob:
    jarFileUris:
    - gs://dataproc-demo-bucket/dataprocJavaDemo-1.0-SNAPSHOT.jar
    mainClass: org.example.dataproc.InternationalLoansAppDataprocLarge
  stepId: ibrd-large-spark
- pysparkJob:
    args:
    - gs://dataproc-demo-bucket
    - ibrd-statement-of-loans-historical-data.csv
    - ibrd-summary-large-python
    mainPythonFileUri: gs://dataproc-demo-bucket/international_loans_dataproc.py
  stepId: ibrd-large-pyspark
placement:
  managedCluster:
    clusterName: three-node-cluster
    config:
      gceClusterConfig:
        zoneUri: us-east1-b
      masterConfig:
        diskConfig:
          bootDiskSizeGb: 500
        machineTypeUri: n1-standard-4
      softwareConfig:
        imageVersion: 1.3-deb9
      workerConfig:
        diskConfig:
          bootDiskSizeGb: 500
        machineTypeUri: n1-standard-4
        numInstances: 2
```

vi my_parametrized_template.yaml

```yaml
...
jobs:
- pysparkJob:
    args:
    - storage_bucket_parameter
    - data_file_parameter
    - results_directory_parameter
    mainPythonFileUri: main_python_file_parameter
  stepId: ibrd-pyspark
placement:
  managedCluster:
    clusterName: three-node-cluster
    config:
      gceClusterConfig:
        zoneUri: us-east1-b
      masterConfig:
        diskConfig:
          bootDiskSizeGb: 500
        machineTypeUri: n1-standard-4
      softwareConfig:
        imageVersion: 1.3-deb9
      workerConfig:
        diskConfig:
          bootDiskSizeGb: 500
        machineTypeUri: n1-standard-4
        numInstances: 2
parameters:
- description: Python script to run
  fields:
  - jobs['ibrd-pyspark'].pysparkJob.mainPythonFileUri
  name: MAIN_PYTHON_FILE
- description: Storage bucket location of data file and results
  fields:
  - jobs['ibrd-pyspark'].pysparkJob.args[0]
  name: STORAGE_BUCKET
  validation:
    regex:
      regexes:
      - gs://.*
- description: IBRD data file
  fields:
  - jobs['ibrd-pyspark'].pysparkJob.args[1]
  name: IBRD_DATA_FILE
- description: Result directory
  fields:
  - jobs['ibrd-pyspark'].pysparkJob.args[2]
  name: RESULTS_DIRECTORY
```


```bash
# import template
gcloud dataproc workflow-templates import my-template \
    --source=my_template.yaml

#instantiate template with args
gcloud dataproc workflow-templates instantiate my-template \
    --parameters=INPUT_FILE=gs://my-bucket/test.txt,OUTPUT_DIR=gs://my-bucket/output/

```

Terminating a workflow

```bash
gcloud dataproc operations cancel operation-id \
    --region=region
```

Deleting a workflow

```bash
gcloud dataproc workflow-templates delete template-id \
    --region=region
```