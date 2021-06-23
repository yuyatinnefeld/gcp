# Google Cloud Platform SDK
> https://console.cloud.google.com/


## SDK command-line tool cheat sheet
> https://cloud.google.com/sdk/docs/cheatsheet


## GCP SDK CLI Tools
- gsutil: Cloud Storage
- bg: BigQuery
- gcloud: rest of GCP products

## GCP SDK Setup (With Docker)

### define ENV variables 
```bash
PROJECT=xxxxx
REGION=xxxxx
ZONE=xxxxx
PROJECT_ID=xxxxx
```

### your GCP Project and activate Compute Engine API

## create GCP SDK container
```bash
docker pull gcr.io/google.com/cloudsdktool/cloud-sdk:latest
docker run --rm gcr.io/google.com/cloudsdktool/cloud-sdk:266.0.0 gcloud version
docker run -ti --name gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud auth login
```
## run docker container
```bash
docker container start gcloud-config
```

## define alias in .bashrc
```bash
alias gcp='docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk'
```

## test
```bash
gcloud version
```

## create GCP project
```bash
gcloud projects create ${PROJECT_ID} --name=${PROJECT} --labels=type=learn
```
delete
```bash
gcloud projects delete ${PROJECT_ID}
```

## config setup
```bash
gcloud config set project ${PROJECT}
```

## check
```bash
gcloud config list
```

### Notice
without interaction
> gcp gcloud ....

with interaction
> docker exec -it gcloud-config gcloud ....


### Configuration
```bash
gcloud config list 
gcloud config configurations list
gcloud config set compute/region europe-west3 
gcloud config configurations activate default
gcloud config set project PROJECT_ID
gcloud config getvalue project
gcloud config configurations delete MY_CONF_NAME
gcloud config configurations create MY_CONF_NAME
```

### Components
```bash
gcloud components list
```
