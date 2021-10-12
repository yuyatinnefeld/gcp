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

if __name__ == "__main__":
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.WARN)
    spark = SparkSession.builder.master("local[2]").appName("Engine").getOrCreate()

    argv_num = 2

    with open(sys.argv[1]) as json_data:
        customer_data_list = json.load(json_data)
        print(customer_data_list)

    with open(sys.argv[2]) as json_data:
        product_data_list = json.load(json_data)
        print(product_data_list)

    if len(sys.argv) != argv_num:
        raise Exception(f"Exactly {argv_num} arguments are required: <inputUri> <outputUri>")

    #print("read input data")
    #df_customer = get_input_records_df(customer_data_list)
    #df_product = get_input_records_df(product_data_list)

    #print("join the dfs")
    #join_key_1 = df_customer.segment_number
    #join_key_2 = df_product.target_segment
    #df_joined = get_jonined_df(df_customer, df_product, join_key_1, join_key_2)

    spark.stop()
