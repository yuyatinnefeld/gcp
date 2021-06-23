#IAM

## check the list
```bash
gcloud iam service-accounts list
```

## setup Service Account
```bash
bash iam_setup_sa.sh
```

## details about service account
```bash
gcloud alpha iam service-accounts describe ${SERVICE_ACCOUNT} 
```


## list of service accounts ##
```bash
gcloud iam service-accounts list
```

## create a service account ##
```bash
gcloud alpha iam service-accounts create ${SERVICE_NAME}  --display-name="yu test display name"
```

## activate the service account ##
```bash
gcloud alpha iam service-accounts enable  ${SERVICE_ACCOUNT}
```

## give the service account a role##
```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID}  \
--member="serviceAccount:"${SERVICE_ACCOUNT} \
--role=${ROLE_NAME}
```
