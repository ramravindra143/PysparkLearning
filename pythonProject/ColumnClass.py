from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark =SparkSession.builder.master('local').appName('columnvalue').getOrCreate()

col1 = lit('abcd')
print(type(col1))

data =[('ravi','ram',2000),('raghu','reddy',1000)]
schema =['name','lastname','salary']
df =spark.createDataFrame(data,schema)
df1 =df.withColumn('ColumnCheck',lit('new_value'))
df1.show()
df1.printSchema()
df1.select(df1.salary).show()
df1.select(df1['salary']).show()
df1.select(col('salary')).show()
spark.stop()