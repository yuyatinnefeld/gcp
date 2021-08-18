from google.cloud import bigquery
import datetime

client = bigquery.Client()

def craete_dataset(dataset_name):
    dataset_id = "{0}.{1}".format(client.project, dataset_name)
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "europe-west3"
    dataset = client.create_dataset(dataset, timeout=30)
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


def create_table(project_id: str, dataset: str, table_name: str):
    table_id = project_id+"."+dataset+"."+table_name

    field1_name = "full_name"
    field1_type = "STRING"
    field2_name = "age"
    field2_type = "INTEGER"
    field3_name = "date"
    field3_type = "DATE"

    schema = [
        bigquery.SchemaField(field1_name, field1_type, mode="REQUIRED"),
        bigquery.SchemaField(field2_name, field2_type),
        bigquery.SchemaField(field3_name, field3_type, mode="REQUIRED"),

    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.

    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )


def query_run(my_query: str) -> str:

    query_job = client.query(
        my_query,
        job_config=bigquery.QueryJobConfig(
            labels={"example-label": "example-value"}, maximum_bytes_billed=1000000
        ),
        job_id_prefix="my_job_123_",
    )

    print("The query data:")
    rows = query_job.result()  # Waits for query to finish
    for row in rows:
        print(row.name)

    print("Started job: {}".format(query_job.job_id))
    return query_job.job_id

def job_status_print(job_id, location):
    job = client.get_job(job_id, location=location)

    print("Details for job {} running in {}:".format(job_id, location))
    print(
        "\tType: {}\n\tState: {}\n\tCreated: {}".format(
            job.job_type, job.state, job.created
        )
    )

def job_listing():

    print("Last 10 jobs:")
    for job in client.list_jobs(max_results=10):
        print("{}".format(job.job_id))

    print("Jobs from the last ten minutes:")
    ten_mins_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
    for job in client.list_jobs(min_creation_time=ten_mins_ago):
        print("{}".format(job.job_id))

    print("Last 10 jobs run by all users:")
    for job in client.list_jobs(max_results=10, all_users=True):
        print("{} run by user: {}".format(job.job_id, job.user_email))

    print("Last 10 jobs done:")
    for job in client.list_jobs(max_results=10, state_filter="DONE"):
        print("{}".format(job.job_id))


def copy_table(table_ids: str, new_table_id: str):
    job = client.copy_table(table_ids, new_table_id)
    job.result()
    print("The tables {} have been appended to {}".format(table_ids, new_table_id))


def delete_table(table_id: str):
    client.delete_table(table_id, not_found_ok=True)
    print("Deleted table '{}'.".format(table_id))