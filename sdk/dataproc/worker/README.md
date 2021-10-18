# Worker nodes


## preemptible vs non preemptible worker
- preemptible worker = PVM (preemptible VM)
- the default dataproc worker is preemptible
- Google can shut down the PVM should additional capacity be required to run other workloads. 
- PVMs work best for testing, quick batch jobs and applications that are fault tolerant. 
- a preemptible VM can save customers up to 80% over a standard Compute Engine instance.
    
- the number of preemptible workers should be less than 50% of the total number of all workers (primary plus all secondary workers)
- the preemptible instances have lower per-hour compute costs
- non-preemptible workers have more job stability (less task fauileres) than preemptible workers
- a cluster can contain either preemptible secondary workers or non-preemptible secondary workers, but not both.
- update of the worker number is possible, but not the type of secondary workers


## REWE VPN Tunneling
--subnet projects/project-id/regions/region/subnetworks/subnetwork-name \

## Configuration
```bash
# create dataproc cluster with 0 secoundary workers
gcloud dataproc clusters create my-test-cluster \
    --num-secondary-workers=0 \
    --region=us-central1

# create dataproc clusters with preemptible secoundary workers
gcloud dataproc clusters create my-test-cluster \
    --num-secondary-workers=2 \
    --region=us-central1


# create dataproc clusters with non preemptible secoundary workers
gcloud dataproc clusters create my-test-cluster \
    --num-secondary-workers=2 \
    --secondary-worker-type=non-preemptible \
    --region=us-central1


# update dataproc clusters
gcloud dataproc clusters update my-test-cluster \
    --num-secondary-workers=5 \
    --region=us-central1

# create dataproc clusters with jupyter notebook
gcloud dataproc clusters create cluster-name \
    --optional-components=ANACONDA, JUPYTER \
    --region=region \
    --enable-component-gateway \
    ... other flags


# ssh connect into the dataproc master node
export PROJECT="my-cluster-39080294-m";export HOSTNAME="yygcplearning";export ZONE="europe-west3-b"
export PORT=1080

gcloud compute ssh ${HOSTNAME} \
    --project=${PROJECT} --zone=${ZONE}  -- \
    -D ${PORT} -N

# create cluster with details 
gcloud dataproc clusters create my-cluster-39080294 \
    --enable-component-gateway
    --bucket demo-dataproc-bucket-31937 \
    --region europe-west3 --zone europe-west3-b \
    --master-machine-type n1-standard-4 \
    --master-boot-disk-size 500 \
    --num-workers 2 \
    --worker-machine-type n1-standard-4 \
    --worker-boot-disk-size 100 \
    --image-version 2.0-debian10 \
    --optional-components JUPYTER, ZEPPELIN \
    --labels project=demo-project,team=demo-team \
    --project yygcplearning
```