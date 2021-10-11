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


if __name__ == "__main__":
    logger = logging.getLogger("py4j")    
    logger.setLevel(logging.WARN)
    spark = SparkSession.builder.master("local[2]").appName("Engine").getOrCreate()
    print("✨ data proc spark started✨")
    spark.stop()
    print("✨ data proc spark stopped")
