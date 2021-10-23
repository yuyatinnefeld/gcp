#!/bin/bash

TEMPLATE_ID="my_workflow_template_id_1234"
REGION="europe-west1"
ZONE="europe-west1-b"

# check the UUID
CLUSTER_UUID=$(gcloud dataproc clusters describe $CLUSTER_2 \
  --region $REGION \
  | grep 'goog-dataproc-cluster-uuid:' \
  | sed 's/.* //')

echo $CLUSTER_UUID

# adjust an existing cluster
gcloud dataproc workflow-templates set-cluster-selector \
  $TEMPLATE_ID \
  --region $REGION \
  --cluster-labels goog-dataproc-cluster-uuid=$CLUSTER_UUID