#!/bin/bash

TEMPLATE_ID="my_workflow_template_id_1234"
REGION="europe-west1"
ZONE="europe-west1-b"
CLUSTER_NAME="demo-three-node-cluster-1234"

# create a template
gcloud dataproc workflow-templates create ${TEMPLATE_ID} \
    --region=${REGION} --labels="project=demo-dataproc"


# set a managed cluster
gcloud dataproc workflow-templates set-managed-cluster \
  $TEMPLATE_ID \
  --region ${REGION} \
  --zone ${ZONE} \
  --cluster-name ${CLUSTER_NAME} \
  --master-machine-type n1-standard-4 \
  --master-boot-disk-size 500 \
  --worker-machine-type n1-standard-4 \
  --worker-boot-disk-size 500 \
  --num-workers 2 \
  --image-version 1.3-deb9