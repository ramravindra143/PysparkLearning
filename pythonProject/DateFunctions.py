from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import *
spark =SparkSession.builder.master('local').appName('datefunctions').enableHiveSupport().getOrCreate()

data =[('ram','ravindra'),('ravi','raghu')]
schema =['firstname','lastname']
df =spark.createDataFrame(data,schema)
df1=df.withColumn('current_date',current_date()).withColumn('current_timestamp',current_timestamp())
df1.show()
df1.printSchema()

##Date formats
