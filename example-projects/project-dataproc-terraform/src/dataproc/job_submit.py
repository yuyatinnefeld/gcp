def submit_pyspark_job(dataproc, project, region, cluster_name, bucket_name, filename):
    """Submit the Pyspark job to the cluster (assumes `filename` was uploaded
    to `bucket_name."""
    job_details = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {
            "main_python_file_uri": "gs://{}/{}".format(bucket_name, filename)
        },
    }

    result = dataproc.submit_job(
        request={"project_id": project, "region": region, "job": job_details}
    )
    job_id = result.reference.job_id
    print("Submitted job ID {}.".format(job_id))
    return job_id
