from util import *
from datetime import datetime
from pytz import timezone

project_id = "bigquery-sandbox-323313"
regional_location="europe-west3"
multi_location="EU"
dataset_1 = "ds_eu"
dataset_2 = "ds_us"
table_1 = "covid"
table_2 = "tb2"

table_id1 = str("{0}.{1}.{2}").format(project_id, dataset_1, table_1)
table_id2 = str("{0}.{1}.{2}").format(project_id, dataset_1, table_2)
table_ids = [table_id1]

print(table_id1)
print(table_id2)

if __name__ == "__main__":

    #craete_dataset(dataset_1)
    #craete_dataset(dataset_2)

    #create_sample_table(dataset_1, table_1)
    #create_sample_table(dataset_1, table_2)

    #create_sample_clustering_table(dataset_2, table_1)

    public_dataset_table = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100'
    )

    col1 = "day"
    col2 = "month"

    my_custom_small_table = str(
    """SELECT {0}, {1} FROM `{2}.{3}.{4}` LIMIT 100"""
    ).format(col1, col2, project_id, dataset_1, table_1)

    #job_id = query_run(my_custom_small_table)

    #job_status_print(job_id, "EU")

    #job_listing()

    #copy_table(table_ids, "project_id.dataset.tb1")

    #delete_dataset("ds_us")
    #delete_table(table_id1)