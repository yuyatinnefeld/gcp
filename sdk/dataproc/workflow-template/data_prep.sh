#!/bin/bash

BUCKET_NAME="gs://dataproc-temp-yt-123456"

# create a temp dir and install tranings data in the dir
mkdir temp                       
cd temp                            
curl -LO http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
unzip trainingandtestdata.zip    
rm trainingandtestdata.zip test*.csv
cd ..
python src/train_test_split.py

# delete temporary directory and the files in it
rm -rf temp

# minimize the training_data.csv and test_data.csv

#rename the files and upload these to GCS
gsutil cp pyspark_sa_train_data.csv gs://${BUCKET_NAME}/input/data/training_data.csv
gsutil cp pyspark_sa_test_data.csv gs://${BUCKET_NAME}/input/data/test_data.csv

# remove the training_data and test_data after uploading
rm pyspark_sa_train_data.csv pyspark_sa_test_data.csv