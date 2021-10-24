# Dataproc Workflow Template
 Workflow is an operation that runs a Directed Acyclic Graph (DAG) of jobs on a cluster. If the workflow uses a managed cluster, it creates the cluster, runs the jobs, and then deletes the cluster when the jobs are finished.

- provides a flexible and easy-to-use mechanism for managing and executing workflows
- automates Spark and Hadoop Workloads on GCP
- ideal for automating large batches of dynamic Spark and Hadoop jobs, and for long-running and unattended job execution, such as overnight.
- managed cluster is ephemeral cluster

## Info
- https://cloud.google.com/dataproc/docs/concepts/workflows/overview
- https://garystafford.medium.com/using-the-google-cloud-dataproc-workflowtemplates-api-to-automate-spark-and-hadoop-workloads-on-gcp-95b02f54b5f2
- https://cloud.google.com/dataproc/docs/tutorials/workflow-composer

## Process
- step1: create a workflow template (API or YAML)
- step2: create a managed cluster or select an existing cluster as managed cluster
- step3: add jobs
- step4: instantiate the template

## initial setup
```bash
./gcp_setup.sh
```

## option 1 - Create a Workflow Templates via. gcloud SDK
```bash
# create a new dataproc with the workflow template
./workflow-temp-api/create-workflow-temp.sh

# alternative (add the workflow template in an exsiting cluster)
./workflow-temp-api/adjust-workflow-temp.sh

#check the template
gcloud dataproc workflow-templates list --region ${REGION}
gcloud dataproc workflow-templates describe ${TEMPLATE_ID} --region ${REGION}

# add job
./workflow-temp-api/add-job-temp.sh

# check if the workflow template has 2 jobs
gcloud dataproc workflow-templates list --region ${REGION}

# check the job config of the workflow template
gcloud dataproc workflow-templates describe ${TEMPLATE_ID} --region ${REGION}

# run the workflow-template jobs
time gcloud dataproc workflow-templates instantiate ${TEMPLATE_ID} --region ${REGION} #--async

# export the template
gcloud dataproc workflow-templates export ${TEMPLATE_ID} \
  --destination my-workflow-template-1.yaml \
  --region ${REGION}
```


## option 2 - Create a Workflow Template via YAML file

```bash
TEMPLATE_ID="my_workflow_template_id_9876"
REGION="europe-west1"

# create a config file
cat resources/my-workflow-template-1.yml

# import template
gcloud dataproc workflow-templates import ${TEMPLATE_ID} \
    --source=my-workflow-template-1.yaml \
    --region=${REGION}

# instantiate template with args
time gcloud dataproc workflow-templates instantiate ${TEMPLATE_ID} --region ${REGION} #--async

# terminating a workflow
gcloud dataproc operations cancel ${OPERATION_ID} --region=region

# delete workflow-template
gcloud dataproc workflow-templates delete ${TEMPLATE_ID} --region=${REGION}
```

## advanced - create a ML prediction model spark

```bash
TEMPLATE_ID="my_workflow_template_id_9876"
REGION="europe-west1"

# prep the data
data_prep.sh

# create a new dataproc with the workflow template
./workflow-temp-api/create-workflow-temp.sh

# add the job3 - ml spark jopb
./add-job-temp.sh

# instantiate template with args
gcloud dataproc workflow-templates instantiate ${TEMPLATE_ID} --region ${REGION} #--async

# export the template
gcloud dataproc workflow-templates export ${TEMPLATE_ID} \
  --destination my-workflow-template-2.yaml \
  --region ${REGION}


# delete workflow-template
gcloud dataproc workflow-templates delete ${TEMPLATE_ID} --region=${REGION}
```