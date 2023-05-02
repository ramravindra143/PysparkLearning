from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark =SparkSession.builder.master('local').appName('udf').getOrCreate()

data= ['Ravindra Reddy','Saritha Reddy']
schema =['first_name','last_name']

rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())
for item in rdd.collect():
    print(item)

#rdd1=rdd.map(lambda x:x.split(' '))

rdd2=rdd.flatMap(lambda x: x.split(' '))

for item in rdd2.collect():
    print(item)
print(rdd2.collect())

#df =spark.createDataFrame(rdd2,schema)
#df.show()
#df.printSchema()
