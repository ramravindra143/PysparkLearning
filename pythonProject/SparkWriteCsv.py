from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql import dataframe
spark =SparkSession.builder.master('local').appName('dataframeWrite').getOrCreate()
print(spark)

schema2 =StructType().add(field='empid',data_type=IntegerType())\
    .add(field='Ename',data_type=StringType())\
    .add(field='Salary',data_type=DecimalType())\
    .add(field='Designation',data_type=StringType())
df4 = spark.read.csv('C://Users//Dell//Desktop//data1//',header=True,inferSchema=True)
df4.show()
df4.printSchema()

#help(df4.write)
#df4.write.csv('C://Users//Dell//Desktop//output',header=True,sep='|')

df5 = spark.read.csv('C://Users//Dell//Desktop//output',header=True,sep='|',inferSchema=True)

df5.show(10,truncate=100)
df5.printSchema()


