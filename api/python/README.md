#Python GCP API

## Setup
### 0. activate venv
```bash
python -m venv ./venv
source ./venv/bin/activate (Mac) or env\Scripts\activate (Windows)
```
### 1. create a GCP project and activate the cloud storage & cloud storage API

### 2. create a GCP service account (From the Role list, select Project > Owner.)

### 3. download the service account json key

### 4. provide authentication credentials to your application code by setting the environment variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/.../python/conf/service_account.json
```


### 5. installing the python client library

cloud storage
```bash
pip install --upgrade google-cloud-storage
```

bigquery
```bash
pip install --upgrade google-cloud-bigquery
```





