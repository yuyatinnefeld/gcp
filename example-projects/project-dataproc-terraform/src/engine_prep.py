import json
import sys
import logging
import pyspark
from typing import Final
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.functions import when
from datetime import date


def get_input_records_df(input_records_files: str) -> pyspark.sql.dataframe.DataFrame:
    """This function imports and transforms all 'input records' files and returns them in the df format"""
    df = spark.read.json(input_records_files)
    print("✨ the input records df is created ✨")
    df.show(truncate=False)
    return df


def get_jonined_df(df_1, df_2, join_key_1, join_key_2) -> pyspark.sql.dataframe.DataFrame:
    """This function creates a joined table of the 'df_1' and the 'df_2'."""
    df_joined = df_1.join(df_2, join_key_1 == join_key_2)
    df_joined = df_joined.sort(join_key_2.asc())
    print("✨ the 2 dfs are joined ✨")
    df_joined.show(truncate=False)
    return df_joined


def save_result_json(df_output: pyspark.sql.dataframe.DataFrame, output_file_name: str):
    """This function exports the result in the JSONL format"""
    pandasDF = df_output.toPandas()
    json_output = pandasDF.to_json(orient="records")[1:-1].replace("},{", "} {")
    with open(output_file_name, "w") as f:
        f.write(json_output)
    print("🎉 the output file is stored in jsonl format 🎉")


if __name__ == "__main__":
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.WARN)
    spark = SparkSession.builder.master("local[2]").appName("Engine").getOrCreate()

    customer_data_list=json.loads(sys.argv[1])
    store_data_list=json.loads(sys.argv[2])
    product_data_list=json.loads(sys.argv[3])
    #output_uri=sys.argv[4]
    argv_num = 3

    if len(sys.argv) != argv_num:
        raise Exception("Exactly 4 arguments are required: <inputUri> <outputUri>")

    #customer_data_list: Final[str] = "gs://test-input-data/customer*.jsonl"     #test-data/customer*.jsonl" 
    #store_data_list: Final[str] =  "gs://test-input-data/store*.jsonl"          #"test-data/store*.jsonl"
    #product_data_list: Final[str] = "gs://test-input-data/product*.jsonl"       #test-data/product*.jsonl

    df_customer = get_input_records_df(customer_data_list)
    df_store = get_input_records_df(store_data_list)
    df_product = get_input_records_df(product_data_list)

    join_key_1 = df_customer.segment_number
    join_key_2 = df_product.target_segment
    df_joined = get_jonined_df(df_customer, df_product, join_key_1, join_key_2)

    join_key_1 = df_joined.visited_store
    join_key_2 = df_store.store_id
    df_joined = get_jonined_df(df_joined, df_store, join_key_1, join_key_2)

    #today = date.today()
    #output_file_name = f"gs://test-output-data/output_{today}.jsonl" #"test-data/output_{today}.jsonl 
    #save_result_json(df_joined, output_file_name)
    #df_joined.saveAsTextFile(sys.argv[4])

    spark.stop()
