#!/bin/bash

REGION="europe-west3"
LOCATION="EU"
ZONE="europe-west3-b"
PROJECT_ID="yygcplearning"
STORAGE_CLASS="Standard"
DATASET="ds_eu"
TABLE_NAME1="tb1"
TABLE_NAME2="tb2"
EXPIRATION=36000
SCHEMA1='ts:TIMESTAMP,qtr:STRING,sales:FLOAT'
SCHEMA2='qtr:STRING,sales:FLOAT,year:STRING'
SCHEMA3='customer_id:INTEGER,qtr:STRING,sales:FLOAT'
UNIT_TIME1=HOUR
UNIT_TIME2=DAY
PARTITION_COLUMN=ts
PARTITION_RANGE=customer_id,0,100,10

# create a time-unit column-partitioned table
bq mk -t \
  --schema ${SCHEMA1} \
  --time_partitioning_type ${UNIT_TIME1} \
  --time_partitioning_expiration ${EXPIRATION} \
  ${DATASET}.${TABLE_NAME1}

SQL:
INSERT INTO
  project_id.dataset.mytable (_PARTITIONTIME,
    field1,
    field2)
SELECT
  TIMESTAMP("2017-05-01 21:30:00"),
  1,
  "one"


# create an ingestion-time partitioned table
bq mk -t \
  --schema ${SCHEMA2} \
  --time_partitioning_type ${UNIT_TIME2} \
  --time_partitioning_expiration ${EXPIRATION}  \
  ${DATASET}.${TABLE_NAME2}

bq mk -t \
  --schema qtr:STRING,sales:FLOAT,year:STRING \
  --time_partitioning_type DAY \
  --time_partitioning_expiration 259200 \
  ds_eu.mytable


# create an integer-range partitioned table
bq mk \
  --schema ${SCHEMA3} \
  --range_partitioning=${PARTITION_RANGE} \
  --require_partition_filter=BOOLEAN  \
  ${DATASET}.${TABLE_NAME1}