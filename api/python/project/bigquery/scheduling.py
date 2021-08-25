from google.cloud import bigquery
import datetime

client = bigquery.Client()

def setup_scheduling(project_id: str, dataset_id: str):

    service_account_name = "rewe-test@bigquery-sandbox-323313.iam.gserviceaccount.com"

    # Use standard SQL syntax for the query.
    query_string = """
    SELECT
    CURRENT_TIMESTAMP() as current_time,
    @run_time as intended_run_time,
    @run_date as intended_run_date,
    17 as some_integer
    """

    parent = transfer_client.common_project_path(project_id)

    transfer_config = bigquery_datatransfer.TransferConfig(
        destination_dataset_id=dataset_id,
        display_name="Your Scheduled Query Name",
        data_source_id="scheduled_query",
        params={
            "query": query_string,
            "destination_table_name_template": "your_table_{run_date}",
            "write_disposition": "WRITE_TRUNCATE",
            "partitioning_field": "",
        },
        schedule="every 24 hours",
    )

    transfer_config = transfer_client.create_transfer_config(
        bigquery_datatransfer.CreateTransferConfigRequest(
            parent=parent,
            transfer_config=transfer_config,
            service_account_name=service_account_name,
        )
    )

    print("Created scheduled query '{}'".format(transfer_config.name))
