# Cloud Logging

Activate API by GCP
> Cloud Logging API

```bash
gcloud logging write my-project-log "My test simple Log: 200:yes"
gcloud logging write my-project-log "My second test simple Log: 200:yesyes"
gcloud logging write --payload-type=json my-projeeeect-log '{"message":"todays wether is ok", "degrees": "30°C"}'
gcloud logging write --payload-type=json my-projeeeect-log '{"message":"todays wether is not ok", "degrees": "10°C"}'
```
> gcp gcloud logging read "resource.type=global"