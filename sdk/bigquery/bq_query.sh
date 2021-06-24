#!/bin/bash

PROJECT="mytestproject"
REGION="europe-west3"
ZONE="europe-west3-b"
PROJECT_ID="mytestproject-20210615"
STORAGE_CLASS="Standard"
BUCKET_NAME="yuyabucket_12345"
DATASET="dataset_20210615"
TABLE_NAME1="ratings"
FILE_NAME_2="movies.csv"

docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq query \
    --use_legacy_sql=false \
    '
    SELECT userId, ratings.movieId, title, genres, rating
    FROM `mytestproject-20210615.dataset_20210615.ratings` AS ratings
    JOIN `mytestproject-20210615.dataset_20210615.movies` AS movies
    ON ratings.movieId = movies.movieId
    '

# the dataset "tmp" must be default and NOT europe
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk \
bq query \
    --use_legacy_sql=false \
    '
    CREATE TABLE tmp.test_arquet_export AS
    SELECT * FROM bigquery-public-data.samples.wikipedia LIMIT 100;
    '

