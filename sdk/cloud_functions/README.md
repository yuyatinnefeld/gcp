# Cloud Functions

## Info
- https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/functions/helloworld

## Setup 
```bash
# create functions 
vi main.py
vi requirements.txt

# deploy the functions
gcloud functions deploy hello_http --runtime python39 --trigger-http --allow-unauthenticated --region europe-west3

# function test
gcloud functions describe hello_http
```

<!-- open the URL -->
https://$GCP_REGION-$PROJECT_ID.cloudfunctions.net/hello_http?name=$TEST_VALUE

example:
- TEST_VALUE="yumyum-wurst"
- GCP_REGION="us-central1"
- PROJECT_ID="yygcplearning"


```bash
# check the logs
gcloud functions logs read hello_http
```

trigger event:
- ex. {"name":"testooomatoo"}
