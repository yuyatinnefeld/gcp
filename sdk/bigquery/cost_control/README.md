# BigQuery Cost Controlling

Cost estimate methods:
- Query validator in the Cloud Console
- --dry_run flag in the bq command-line tool
- dryRun parameter when submitting a query job using the API
- The Google Cloud Pricing Calculator
- Client libraries


```bash
bq query \
--use_legacy_sql=false \
--dry_run \
'SELECT * FROM `project_id.dataset.table`'
```
## Estimate Query Cost
Caluculator: https://cloud.google.com/products/calculator

### On-demand plan
If you use on-demand billing, BigQuery charges for data manipulation language (DML) statements based on the number of bytes processed by the statement.

DDL statements
- CREATE TABLE    None.
- CREATE VIEW     None.
- DROP TABLE      None.
- DROP VIEW 	  None.

DML statements
- INSERT 	q
- UPDATE 	q + t
- DELETE 	q + t
- MERGE 	If there are only INSERT clauses: q. If there is an UPDATE or DELETE clause: q + t.


- q = The sum of bytes processed for the columns referenced in the tables scanned by the query.
- t = The sum of bytes for all columns in the updated table, at the time the query starts, regardless of whether those columns are referenced or modified in the query.

#### Clustered tables
Clustered tables can help you to reduce query costs by pruning data so it is not processed by the query. This process is called block pruning.

##### Block pruning
BigQuery sorts the data in a clustered table based on the values in the clustering columns and organizes them into blocks.

##### Querying columnar formats on Cloud Storage
If your external data is stored in ORC or Parquet, the number of bytes charged is limited to the columns that BigQuery reads. Because the data types from an external data source are converted to BigQuery data types by the query, the number of bytes read is computed based on the size of BigQuery data types.

## Setup the Cost Control

## Creating a custom quotas
- project-level or user-level
- Ex. 
    - Project-level: 50 TB per day
    - User-level: 10 TB per day

## Best Practices for controlling cost
- Avoid SELECT * / query only the columns you need
- Partitioning your tables by date
- Use Clustering if you can
- Don't run queries to explore or preview table data. > Use the Preview Tab
- In the bq command-line tool, use the bq head command
- In the API, use tabledata.list to retrieve table data
- Before running queries, preview them to estimate costs
- Limit query costs by restricting the number of bytes billed (--maximum_bytes_billed=1000000)
- [Create a dashboard to view your billing data](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#how-to-enable)
- Use streaming inserts only if your data must be immediately available


