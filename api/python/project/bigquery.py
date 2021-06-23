from google.cloud import bigquery

client = bigquery.Client()

def query(my_query):

    query_job = client.query(my_query)

    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("PRODUCT={}, PRICE={}, DISCOUNT={}".format(row["PRODUCT"], row["PRICE"], row["DISCOUNT"]))