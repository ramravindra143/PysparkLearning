
from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[1]").appName("SparkByExamples").getOrCreate()
    # Create RDD from parallelize
    dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
    rdd = spark.sparkContext.parallelize(dataList)
    rdd.take(2)

