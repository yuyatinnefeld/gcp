# GCP Project 5 - Classifying Images of Clouds in the Cloud with Vision

## About
- Upload a labeled dataset to Cloud Storage and connect it to AutoML Vision with a CSV label file
- Train a model with AutoML Vision and evaluate its accuracy
- Generate predictions on your trained model

## Info
- Data: gs://cloud-training/automl-lab-clouds/*
- GCP Services: Pub/Sub, Dataflow, BigQuery, Data Studio

## Enable APIs and Services
- Cloud AutoML API


## Create a Cloud Storage bucket and Upload the data

```bash
BUCKET_NAME=$DEVSHELL_PROJECT_ID-vcm

# create a cloud storage bucket
gsutil mb -p $DEVSHELL_PROJECT_ID \
    -c regional    \
    -l us-central1 \
    gs://$BUCKET_NAME/

# copy files

gsutil -m cp -r gs://cloud-training/automl-lab-clouds/* gs://$BUCKET_NAME/


# check the files
gsutil ls gs://$BUCKET_NAME/
```

## Create an AutoML Version Training Dataset

```bash
gsutil cp gs://cloud-training/automl-lab-clouds/data.csv .
head --lines=10 data.csv
sed -i -e "s/placeholder/$BUCKET_NAME/g" ./data.csv
head --lines=10 data.csv
gsutil cp ./data.csv gs://$BUCKET_NAME/
gsutil ls gs://$BUCKET_NAME/

# check the data.csv
gsutil ls gs://$BUCKET_NAME/*
```

Open Vision 
> https://console.cloud.google.com/vision/datasets

1. At the top of the Cloud Console, click + New dataset.
- dataset name: clouds
- model pbjective: Single-Label Classification

2. Choose location of your training  images
3. Choose Select a CSV file on Cloud Storage
4. Add the file name to the URL for the file that is in your clipboard from the previous step
```
gs://
$BUCKET_NAME/data.csv
```

It will take 8 to 12 minutes while the image metadata is processed ("Running: Importing Images" will appear on the screen). Once complete, the images will appear by category.


## Inspect the images
check pics

## Train your model
1. To train your clouds model, go to the Train tab and click Start training.
2. Leave Cloud hosted selected and click Continue.
3. For the next step, type the value "8" into the Set your budget * box
4. Check Deploy model to 1 node after training. 

Note: Training this custom model can be expected to take over an hour to complete (55 to 90 minutes on average). The total training time includes node training time as well as infrastructure set up and tear down.

## Evaluate your model
Finally, scroll down to take a look at the Confusion matrix.

## Generate prediction 
1. Select the model
2. Click Upload images and upload the cloud sample images you just saved to your local disk.