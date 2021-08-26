from google_auth_oauthlib import flow
from google.cloud import bigquery


launch_browser = True

appflow = flow.InstalledAppFlow.from_client_secrets_file(
    "conf/client_secret_oauth.json", scopes=["https://www.googleapis.com/auth/bigquery"]
)

if launch_browser:
    appflow.run_local_server()
else:
    appflow.run_console()

credentials = appflow.credentials
project = 'yygcplearning'


client = bigquery.Client(project=project, credentials=credentials)

print("Last 10 jobs run by all users:")
for job in client.list_jobs(max_results=10, all_users=True):
    print("{} run by user: {}".format(job.job_id, job.user_email))
    