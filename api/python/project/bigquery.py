from google.cloud import bigquery

client = bigquery.Client()

def query(my_query):

    query_job = client.query(my_query)

    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("PRODUCT={}, PRICE={}, DISCOUNT={}".format(row["PRODUCT"], row["PRICE"], row["DISCOUNT"]))


def create_table(project_id, dataset, table_name):
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

def copy_table(table_ids, new_table_id):
    job = client.copy_table(table_ids, new_table_id)
    job.result()
    print("The tables {} have been appended to {}".format(table_ids, new_table_id))


def delete_table(table_id):
    client.delete_table(table_id, not_found_ok=True)
    print("Deleted table '{}'.".format(table_id))