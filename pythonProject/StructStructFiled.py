from pyspark.sql import *
from pyspark.sql.types import *
spark=SparkSession.builder.master('local').appName('StructField').getOrCreate()
data =[()]