from google_auth_oauthlib import flow
from google.cloud import bigquery


def get_credentials(credential_path):
    launch_browser = True

    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        credential_path, scopes=["https://www.googleapis.com/auth/bigquery"]
    )

    if launch_browser:
        appflow.run_local_server()
    else:
        appflow.run_console()

    credentials = appflow.credentials

    return credentials

def show_query_jobs(credentials, project_id, job_results_count):
    client = bigquery.Client(project=project_id, credentials=credentials)

    print("Last {} jobs run by all users:".format(job_results_count))

    sum_bytes_billed = 0
    sum_bytes_processed = 0

    for idx, job in enumerate(client.list_jobs(max_results=job_results_count, all_users=True)):
        #https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.QueryJob.html

        print("#######################################")
        print("Job: {}".format(idx))
        print("Job ID: {}".format(job.job_id))
        print("Job Type: {}".format(job.job_type))
        print("Labels: {}".format(job.labels))
        print("State: {}".format(job.state))
        print("Created: {}".format(job.created))
        print("Started: {}".format(job.started))
        print("Ended: {}".format(job.ended))
        print("User: {}".format(job.user_email))

        if(job.job_type == 'query'):
            print("Estimated Bytes Processed: {}".format(job.estimated_bytes_processed))
            print("Total Bytes Billed: {}".format(job.total_bytes_billed))
            print("Total Bytes Processed: {}".format(job.total_bytes_processed))
            print("Query: {}".format(job.query))

            if(isinstance(job.total_bytes_billed, int) and isinstance(job.total_bytes_processed, int)):
                sum_bytes_billed += job.total_bytes_billed
                sum_bytes_processed += job.total_bytes_processed

        if(job.job_type == 'load'):
            print("Input File Bytes: {}".format(job.input_file_bytes))
            print("Input File: {}".format(job.input_files))
            print("Destination Table: {}".format(job.destination))
            print("Schema: {}".format(job.schema))


    print("\n 🤖 ########## Query Bytes Consume ########## 🤖")
    print("Bytes Billed: {}".format(sum_bytes_billed))
    print("Bytes Processed: {}".format(sum_bytes_processed))

if __name__ == "__main__":
    credential_path = "conf/client_secret_oauth.json"
    project_id = "yygcplearning"
    job_results_count=20

    credentials = get_credentials(credential_path)
    show_query_jobs(credentials, project_id, job_results_count)