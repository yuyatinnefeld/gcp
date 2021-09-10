# GEC (Google Compute Engine)

1. connect with your GCP project
```bash
gcloud config set project ${PROJECT}
```
2. create a GCP vm instance
```bash
gcloud compute instances create myinstance --zone=europe-west3-b


NAME        ZONE            MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
myinstance  europe-west3-b  n1-standard-1               10.156.0.2   34.141.87.167  RUNNING
```

3. create a ssh-key for the vm instance
```bash
gcloud compute config-ssh
```
4. go to the instance 
```bash
ssh myinstance.europe-west1-b.yuyatinnefeld-testing
touch a b c
exit
```

5. open SSH Configuration file (VS Code)
```bash
Host gcp-gce
    HostName <GCP External IP>
    IdentityFile ~/.ssh/google_compute_engine
    UserKnownHostsFile= ~/.ssh/google_compute_known_hosts
    HostKeyAlias=compute.123456789123456798
    IdentitiesOnly=yes
    CheckHostIP=no
    User <local-pc-user>

Host gcp-gce
    HostName 34.141.87.167
    IdentityFile /home/ytubuntu/.ssh/google_compute_engine
    UserKnownHostsFile=/home/ytubuntu/.ssh/google_compute_known_hosts
    HostKeyAlias=compute.4583265746303638803
    IdentitiesOnly=yes
    CheckHostIP=no
```
6. connect current window to host (VS Code)

## GCE + pyspark docker image

### Setup a docker vm instance on GCP

1. create a container-optimized GCE instance
```bash
PROJECT_ID=$(gcloud config get-value project)
INSTANCE_NAME="pyspark-docker"
ZONE="europe-west3-b"
IMAGE_NAME="cos-cloud"

# connect to your GCP project
gcloud config set project ${PROJECT_ID}

# create a container GCE vm instance
gcloud compute instances create-with-container ${INSTANCE_NAME} \
    --container-image ${IMAGE_NAME} --zone=${ZONE}

# ssh connect
gcloud beta compute ssh --zone ${ZONE} ${INSTANCE_NAME} --project ${PROJECT_ID}

# test docker
sudo docker ps
sudo docker run hello-world
```

1.2. create a GCE instance and install docker (alternative solution)
```bash
PROJECT_ID=$(gcloud config get-value project)
INSTANCE_NAME="pyspark-docker"
ZONE="europe-west3-b"

# connect to your GCP project
gcloud config set project ${PROJECT_ID}

# create a GCP vm instance
gcloud compute instances create ${INSTANCE_NAME} --zone=${ZONE}

# ssh connect
gcloud beta compute ssh --zone ${ZONE} ${INSTANCE_NAME} --project ${PROJECT_ID}

# install docker engine
sudo apt-get update
sudo apt-get install docker.io

# test docker
sudo docker ps
sudo docker run hello-world
```

2. Create a pyspark container
```bash
docker container run --name pyspark -p 8888:8888 jupyter/pyspark-notebook
```

2.1. open the jupyter notebook URL which is displayed in your terminal
- http://127.0.0.1:8888/?token=xxxxx

2.2. paste the token and set new password

2.3. create a new notebook or import your notebook

3. Use Pyspark in the vm instance

```bash
# container activate
docker contaienr start pyspark

# check the container is running
docker ps

# start docker container bash session
docker exec -it pyspark bash

# start pyspark session
pyspark

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.2
      /_/

Using Python version 3.9.6 (default, Jul 11 2021 03:39:48)
Spark context Web UI available at http://a9e582d60d90:4040
Spark context available as 'sc' (master = local[*], app id = local-1631084757428).
SparkSession available as 'spark'.

>>> sc
<SparkContext master=local[*] appName=PySparkShell>

>>> spark
<pyspark.sql.session.SparkSession object at 0x7f0faa0064c0>

exit
```

```bash
vi pi_calculator.py
```

```python
import pyspark
sc = pyspark.SparkContext('local[*]')

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
```


```bash
python pi_calculator.py
```

4. Delete instance
```bash
gcloud compute instances delete ${INSTANCE_NAME}  --zone=${ZONE}
```
