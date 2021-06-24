from cloud_storage import *
from bigquery import *
from data_generate import create_sample_df
from datetime import datetime
from pytz import timezone

def cloud_storage():
    region = 'Europe/Paris'
    bucket_name = 'yuyas-test-bucket'
    now = datetime.now(timezone(region))
    blob_name = 'input/foods_{}.csv'.format(now.strftime('%Y%m%d%H%M%S'))

    #implicit()
    #list_blobs('yu_bucket_1')
    #create_new_bucket('yu_bucket_2')
    #file_upload('yu_bucket_1', 'yu_test.json', 'local-file.json')
    #copy_blob('yu_bucket_1', 'yu_test.json', 'yu_bucket_2', 'copied_file2.json')
    #rename_blob('yu_bucket_2', 'copied_file.json', 'yu_test_new_name.json')
    #change_file_storage_class('yu_bucket_1', 'yu_test.json', 'NEARLINE')
    #blob_metadata('yu_bucket_1','yu_test.json')
    #delete_blob('yu_bucket_1','cv - yuya tinnefeld - de.pdf')
    #delete_blob('yu_bucket_1','yu_test.json')
    #delete_blob('yu_bucket_2','yu_test_new_name.json')
    #delete_bucket('yu_bucket_1')
    #delete_bucket('yu_bucket_2')

    df = create_sample_df(now)
    upload_csv(bucket_name, blob_name, df)

def bigquery():
    project_id = "xxxx"
    dataset = "yyy"
    table_name = "zzz"
    table_id1 = project_id+"."+dataset+"."+table_name
    table_ids = [table_id1]

    create_table(project_id, dataset,table_name)

    copy_table(table_ids, "gcptraining-314606.EDA.new_hira")

    delete_table(table_id1)

    my_query = """
        SELECT PRODUCT, PRICE, DISCOUNT 
        FROM `gcptraining-314606.EDA.campaigns` 
        LIMIT 100
    """

    query(my_query)


if __name__ == "__main__":
    #bigquery()
    cloud_storage()