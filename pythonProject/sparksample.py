from pyspark.sql import SparkSession
from pyspark.sql.types import *



spark = SparkSession.builder.master('local').appName('spark').getOrCreate()
print("spark object is created")

rdd1 =spark.sparkContext.parallelize([1,2,3])
print(rdd1.take(5))
print(type(rdd1))
print(type(spark))
#print(dir(spark))
#print(help(spark.createDataFrame))

sampleList=[[1,2,3],[1,2,3]]
schema = ['name','empid','ename']
df1 =spark.createDataFrame(data=sampleList,schema=schema)

df1.show(2)
df1.printSchema()
schema1=StructType([StructField('Name',IntegerType(),True),\
               StructField('empname',IntegerType(),True),\
               StructField('sampleid',IntegerType(),True)])
df2 =spark.createDataFrame(data=sampleList,schema=schema1)
df2.show()
df2.printSchema()

print(help(spark.read))