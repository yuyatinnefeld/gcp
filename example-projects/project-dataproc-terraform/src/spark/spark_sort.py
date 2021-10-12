import pyspark
import logging


if __name__ == "__main__":
    sc = pyspark.SparkContext()
    print("✨ data proc spark started✨")
    rdd = sc.parallelize(["Hello,", "world!", "dog", "elephant", "panther"])
    words = sorted(rdd.collect())
    print(words)

    print("✨ get data from the GCS bucket✨")
    rdd = sc.textFile("gs://yygcplearning-spark-project/gitlab/test-input-data/demo.txt")
    print(sorted(rdd.collect()))

    sc.stop()
    print("✨ data proc spark stopped")
