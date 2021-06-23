# OAuth2
![GitHub Logo](/images/oauth.png)

- Resource Owner (User / Google Account)
- Client (cloud SDK or GCP API)
- Resource Server (Service of GCP ex. GCE, GCS, SQL, etc.)
- Authorization Server (GCP)


## AuthN (user identity)
- AuthN is a part of the Oauth2 in the most case
- 3 FA (factor authentication types)
  - Inherence factor (What you are) - ex. fingerprint scan, facial (face) recognition
  - Possession factor (What you have) - ex. one-time-password token
  - Knoweledge factor (What you know) - ex. PIN, User ID, Password

## AuthZ (user identify and service-permission)
- Permission factor (What can you do)
- 2 AuthZ Types
  - user-to-service permission (Authorization Code / Google Account Browser Login / User-Agent) => used oft for the dev env
  - service-to-service-permission (JWT Bear Token / No direct End User) = used oft for the prod env

- 2 AuthZ Instances
  - Cloud SDK (gcloud, gsutil, bq)
  - Server Application (Service Account / GCP Application)

## Auth Flow Diagram
![GitHub Logo](/images/oauth_flow_diagram.png)

>https://darutk.medium.com/diagrams-and-movies-of-all-the-oauth-2-0-flows-194f3c3ade85



## Access Type by GCP

|  | Cloud SDK | Service Application |
| ------------- | ------------- | ------------- |
| User Account  | 1.gcloud auth login  | 3.gcloud auth application-default login  |
| Service Account  | 2.gcloud auth activate-service-account  | 4.Application Default Credentials  |

1. User Account + Cloud SDK

![GitHub Logo](/images/oauth1.png)

```bash
gcloud auth login
```

2. Service Account + Cloud SDK (JWT Bearer Grant)

![GitHub Logo](/images/oauth2.png)

```bash
gcloud auth activate-service-account --key-file=KEY_FILE
```

3. User Account + Service Application

![GitHub Logo](/images/oauth3.png)
   
```bash
gcloud auth application-default login
```

4. Service Account + Service Application

![GitHub Logo](/images/oauth3.png)

> https://cloud.google.com/docs/authentication/production#providing_credentials_to_your_application

## Error

401 Unauthorized => AuthN Error (= who are you?)
403 Forbidden => AuthZ Missing (= the server understood but no!)

