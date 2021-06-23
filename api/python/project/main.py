from cloud_storage import *
from bigquery import *

if __name__ == "__main__":

    ## Google Storage
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


    ## BigQuery

    my_query = """
        SELECT PRODUCT, PRICE, DISCOUNT 
        FROM `gcptraining-314606.EDA.campaigns` 
        LIMIT 100
    """
    query(my_query)
