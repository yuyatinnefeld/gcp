#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyspark
import logging
from pyspark.sql import SparkSession


def main():
    logger = logging.getLogger("py4j")    
    logger.setLevel(logging.WARN)
    spark = SparkSession.builder.master("local[2]").appName("Engine").getOrCreate()
    print("✨ data proc spark started✨")
    spark.stop()
    print("✨ data proc spark stopped")

if __name__ == "__main__":
    main()