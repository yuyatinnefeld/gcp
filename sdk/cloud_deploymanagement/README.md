# Cloud Deployment Manager

## Info
- https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets

## GCE Deploy
```bash
# create a vm configure file
vi two-vms.yml

# deploy 2 GCE instances
gcloud deployment-manager deployments create deployment-with-2-vms --config two-vms.yaml
```

## Cloud Storage Deploy
 ```bash
# create a vm configure file
vi two-gcs.yml

# deploy 2 GCE instances
gcloud deployment-manager deployments create deployment-with-2-vms --config two-gcs.yaml
```