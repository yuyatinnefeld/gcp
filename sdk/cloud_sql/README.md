# SQL

## define ENV variables
```bash
PROJECT="xxxxx"
ZONE="xxxxx"
PROJECT_ID="xxxxx"
PASSWORD="xxxxx"
CPU=x
MEMORY="xxxxx"
DBTYPE="xxxxx"
DBNAME="xxxxx"
```

## create a postgres db
```bash
gcloud sql instances create ${DBNAME}  \
--database-version=${DBTYPE} --cpu=${CPU} --memory=${MEMORY}  \
--zone=${ZONE} --root-password=${PASSWORD}
```

## check the db
```bash
gcloud sql databases list
```

## check the SQL setup
```bash
gcloud sql instances describe ${DBNAME} 
```

## setup iam & role
```bash
cd iam 
bash iam_setup_sa.sh
```

## importing data
```bash
gcloud sql import csv [INSTANCE_NAME] gs://${BUCKET_NAME}/${FILE_NAME} \
--database=${DBNAME}  --table=${TABLE_NAME}                             
```