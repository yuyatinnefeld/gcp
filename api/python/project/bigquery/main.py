from datetime import datetime
from pytz import timezone
from scheduling import *
from util import *


project_id = "bigquery-sandbox-323313"
project_id2 = "yygcplearning"
regional_location="europe-west3"
multi_location="EU"
dataset_1 = "ds_eu"
dataset_2 = "ds_us"
dataset_3 = "ds_delete"
table_1 = "covid"
table_2 = "tb2"

table_id1 = str("{0}.{1}.{2}").format(project_id, dataset_1, table_1)
table_id2 = str("{0}.{1}.{2}").format(project_id, dataset_1, table_2)
table_ids = [table_id1]

if __name__ == "__main__":

    #craete_dataset(dataset_3)
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

    #job_id = interactive_query(my_custom_small_table)
    
    #job_status_print(job_id, "EU")

    #job_listing()

    #batch_query(my_custom_small_table)

    #copy_table(table_ids, "project_id.dataset.tb1")
    #delete_dataset("ds_us")
    #delete_table(table_id1)


    #create_scheduled_query(project_id2, dataset_1)


    ## Delete scheduled queries
    #check the transfer_config_name with the following cmd
    
    #bq ls \
    #--transfer_config \
    #--transfer_location=eu

    tcn1="projects/928012749692/locations/europe/transferConfigs/6127a765-0000-25e1-9405-089e082fdc00"
    tcn2="projects/928012749692/locations/europe/transferConfigs/6127b2f9-0000-2e9a-a324-30fd380f6764"
    tcn3="projects/928012749692/locations/europe/transferConfigs/61421d92-0000-20fd-9a39-089e08213e78"
    transfer_config_list = [tcn1, tcn2, tcn3]
    
    for tcn in transfer_config_list:
        delete_scheduled_query(tcn)