from pyspark.sql import  *
from pyspark.sql.types import *

spark =SparkSession.builder.master('local').appName('SimpleApp').getOrCreate()

data = [(1,'Ravindra',2000),(2,'Ram',4000),(3,'Raghu',3000)]
columns = ['id','name','salary']
df =spark.createDataFrame(data=data,schema=columns)
df.show()
df.printSchema()
df1 =df.withColumnRenamed('salary','salary_amount')
df.printSchema()
df1.printSchema()
