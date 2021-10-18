# Dataproc Job 


## Life Cycle
- Dataproc service: sends job requests to the dataproc agent
- Dataproc agent: receives job requests and generates driver
- Driver: executes Hadoop jar, spark-submit, pig, etc.

## Job Flopw
- step1: service sneds jobs
    - JobStatus.State = PENDING: when the job is submitted

- step2: agent checks the jobs
    - JobStatus.State = RUNNING: the job is acquired by agent
    - JobStatus.State = ERROR: the job is not acquired by agent

- step3: agent checks master node resources to execute the dirver
    - JobStatus.State = QUEUED: resources are not enough and Job.JobStatus.details shows more details

- step4: agent runs job driver process

- step5: agent sends job progress, cluster metrics, YARN application informtion to dataproc service. 

- step6: YARN application completes
    - JobStatus.State = RUNNING

- step7: dirver exits and agent sends the status=DONE to service
    - JobStatus.State = DONE


### Job Monitoring
```bash
gcloud dataproc jobs describe job-id \
    --region=region
```

### Error Reasons
- out-of-memory (OOM)
- network issues


## Restartable jobs 
- Dataproc jobs will NOT automatically restart on failure
- You can set jobs to restart on failure. 
- you can set the max num of retries per hour (max value is 10 retries per hour)
- you can set the max num of total retries (max value is 240 total retries).

### Job semantics
- job = SUCCESSFUL, if the driver terminates with 0
- job = ERROR, if
    - driver terminates with non-zero code more than 5 times in 10 min
    - driver terminates with non-zero code more than max_failures_per_hour or more than max_failures_total
- job = RESTARTED, if the driver exists with non-zero code withhin max_failures_per_hour or max_failures_total

### Create restarted job
```bash
gcloud dataproc jobs submit job type \
    --region=region \
    --max-failures-per-hour=number \
    --max-failures-total=number \
    ... other args
```