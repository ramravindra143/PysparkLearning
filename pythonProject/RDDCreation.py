from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark =SparkSession.builder.master('local').appName('udf').getOrCreate()

data =((1,'Ram','Ravindra',2000,500),(2,'Ravi','Ravindra',2000,300))
schema =['id','fname','lname','salary','hike','full name']
rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())
rdd1=rdd.map(lambda x: x + (x[1]+' '+x[2],))
print(rdd1.collect())

df=rdd1.toDF(schema)
df.show()
df.printSchema()