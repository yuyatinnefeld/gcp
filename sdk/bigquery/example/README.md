# Example

# create a table from a query result

DATASET=ds_eu
TABLE_NAME1=covid

bq query \
--destination_table ${DATASET}.${TABLE_NAME1} \
--label bqsandbox:dev \
--use_legacy_sql=false \
'SELECT 
  * 
FROM `bigquery-public-data.covid19_ecdc_eu.covid_19_geographic_distribution_worldwide` 
LIMIT 100
'
