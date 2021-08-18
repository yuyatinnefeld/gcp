from util import create_table, query_run, delete_table, copy_table, craete_dataset
from datetime import datetime
from pytz import timezone

project_id = "bigquery-sandbox-323313"
dataset_1 = "ds1"
dataset_2 = "ds2"
table_1 = "tb1"
table_2 = "tb2"
table_id1 = project_id+"."+dataset_1+"."+table_1
table_id2 = project_id+"."+dataset_1+"."+table_2
table_ids = [table_id1]


if __name__ == "__main__":

    #craete_dataset(dataset_1)
    #craete_dataset(dataset_2)

    #create_table(project_id, dataset_1, table_1)
    #create_table(project_id, dataset_1, table_2)

    my_query_1 = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100'
    )

    my_query_2 = """
        SELECT PRODUCT, PRICE, DISCOUNT 
        FROM `xxxxxxxxxx.dataset.table` 
        LIMIT 100
    """

    query_run(my_query_1)
    
    #query_run(my_query_2)

    #copy_table(table_ids, "project_id.dataset.tb1")

    #delete_table(table_id1)