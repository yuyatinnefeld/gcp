from google.cloud import storage
storage_client = storage.Client()

def implicit():
    buckets = list(storage_client.list_buckets())
    print(buckets)

def list_blobs(bucket_name):
    # blob_name = "your-object-name"
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)

def create_new_bucket(bucket_name):
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket {} created.".format(bucket.name))

def file_upload(bucket_name, bucket_file_name, local_file_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_file_name)

    with open(local_file_name, 'rb') as f:
        blob.upload_from_file(f)

    print("Upload complete")

def copy_blob(
        bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"
    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


def rename_blob(bucket_name, blob_name, new_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    new_blob = bucket.rename_blob(blob, new_name)

    print("Blob {} has been renamed to {}".format(blob.name, new_blob.name))


def change_file_storage_class(bucket_name, blob_name, storage_class):
    #Storage class => STANDARD, NEARLINE, COLDLINE, ARCHIVE
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    blob.update_storage_class(storage_class)

    print(
        "Blob {} in bucket {} had its storage class set to {}".format(
            blob_name,
            bucket_name,
            blob.storage_class
        )
    )
    return blob

def blob_metadata(bucket_name, blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)

    print("Blob: {}".format(blob.name))
    print("Bucket: {}".format(blob.bucket.name))
    print("Storage class: {}".format(blob.storage_class))
    print("ID: {}".format(blob.id))
    print("Size: {} bytes".format(blob.size))
    print("Updated: {}".format(blob.updated))
    print("Generation: {}".format(blob.generation))
    print("Metageneration: {}".format(blob.metageneration))
    print("Etag: {}".format(blob.etag))
    print("Owner: {}".format(blob.owner))
    print("Component count: {}".format(blob.component_count))
    print("Crc32c: {}".format(blob.crc32c))
    print("md5_hash: {}".format(blob.md5_hash))
    print("Cache-control: {}".format(blob.cache_control))
    print("Content-type: {}".format(blob.content_type))
    print("Content-disposition: {}".format(blob.content_disposition))
    print("Content-encoding: {}".format(blob.content_encoding))
    print("Content-language: {}".format(blob.content_language))
    print("Metadata: {}".format(blob.metadata))
    print("Custom Time: {}".format(blob.custom_time))
    print("Temporary hold: ", "enabled" if blob.temporary_hold else "disabled")
    print(
        "Event based hold: ",
        "enabled" if blob.event_based_hold else "disabled",
    )
    if blob.retention_expiration_time:
        print(
            "retentionExpirationTime: {}".format(
                blob.retention_expiration_time
            )
        )

def delete_blob(bucket_name, blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))

def delete_bucket(bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()
    print("Bucket {} deleted".format(bucket.name))