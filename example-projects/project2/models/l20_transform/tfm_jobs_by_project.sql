SELECT
project_id, job_id, job_type, statement_type, priority,
EXTRACT(DATE FROM start_time) as start_date,
EXTRACT(HOUR FROM start_time) as start_hour,
EXTRACT(MINUTE FROM start_time) as start_minute,
COUNT(query) as  total_query,
SUM(total_bytes_processed) as total_bytes_processed, 
SUM(total_slot_ms) as total_slot_ms,
SUM(total_bytes_billed) as  total_bytes_billed,
SUM(total_slot_ms) / (1000*60*60*24*7) AS avg_slots
FROM {{ref('rawdata_jobs_by_project')}} src
WHERE total_slot_ms > 0
AND end_time BETWEEN TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY) AND CURRENT_TIMESTAMP()
GROUP BY project_id, job_id, job_type, statement_type, priority, query, start_date, start_hour, start_minute