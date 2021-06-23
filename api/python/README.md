#Python GCP API

## Setup
### 0. activate venv
```bash
python -m venv ./venv
source ./venv/bin/activate (Mac) or env\Scripts\activate (Windows)
```
### 1. create GCP project and activate cloud storage & cloud storage API

### 2. create GCP service account (From the Role list, select Project > Owner.)

### 3. download the service account json key

### 4. provide authentication credentials to your application code by setting the environment variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/...YOUR_GCP_PROJECT.../conf/service_account.json
```

### 5. installing the python client library

```bash
pip install --upgrade google-cloud-storage
```





