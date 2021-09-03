from cloud_storage import *
from data_generate import create_sample_df
from datetime import datetime
from pytz import timezone

region = 'Europe/Paris'
bucket_name = 'yygcplearning-ds'
now = datetime.now(timezone(region))
blob_name = 'foods_{}.csv'.format(now.strftime('%Y%m%d%H%M%S'))
file_name = 'yt_test.json'

if __name__ == "__main__":
    #implicit()
    #list_blobs(bucket_name)
    #create_new_bucket(bucket_name)
    #file_upload(bucket_name, file_name, 'local-file.json')
    #copy_blob(bucket_name, file_name, bucket_name, 'copied_file2.json')
    #rename_blob(bucket_name, 'copied_file.json', 'yu_test_new_name.json')
    #change_file_storage_class(bucket_name, file_name, 'NEARLINE')
    #blob_metadata(bucket_name,file_name)
    #delete_blob(bucket_name,'cv - yuya tinnefeld - de.pdf')
    #delete_blob(bucket_name,file_name)
    #delete_blob(bucket_name,'yu_test_new_name.json')
    #delete_bucket(bucket_name)
    #delete_bucket(bucket_name)

    df = create_sample_df(now)
    upload_csv(bucket_name, blob_name, df)