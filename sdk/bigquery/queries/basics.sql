
-- create a small table from the public data

-- location US
CREATE TABLE ds_us.smalltb AS (
    SELECT * FROM `bigquery-public-data.austin_311.311_service_requests` LIMIT 10
)

-- location EU
CREATE TABLE ds_eu.smalltb AS (
    SELECT * FROM `bigquery-public-data.covid19_ecdc_eu.covid_19_geographic_distribution_worldwide` LIMIT 10
)