from util import *
from datetime import datetime
from pytz import timezone

project_id = "bigquery-sandbox-323313"
regional_location="europe-west3"
multi_location="EU"
dataset_1 = "ds_eu"
dataset_2 = "ds_us"
table_1 = "tb1"
table_2 = "tb2"
table_id1 = project_id+"."+dataset_1+"."+table_1
table_id2 = project_id+"."+dataset_1+"."+table_2
table_ids = [table_id1]

if __name__ == "__main__":

    #craete_dataset(dataset_1)
    #craete_dataset(dataset_2)

    #create_sample_table(dataset_1, table_1)
    #create_sample_table(dataset_1, table_2)

    create_sample_clustering_table(dataset_2, table_1)

    public_dataset_table = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100'
    )

    my_custom_small_table = """
        SELECT source, status 
        FROM `bigquery-sandbox-323313.test.smalltb2` 
        LIMIT 100
    """

    #job_id = query_run(my_custom_small_table)

    #job_status_print(job_id, "US")

    #job_listing()

    #copy_table(table_ids, "project_id.dataset.tb1")

    #delete_dataset("ds_us")
    #delete_table(table_id1)