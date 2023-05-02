from pyspark.sql import *
from pyspark.sql.types import  *
from pyspark.sql.functions import *
from pyspark.sql import Row

spark =SparkSession.builder.master('local').appName('rowApp').getOrCreate()

row =Row(name='Ravindra',salary='2000')
print(row[0],row[1])
row1 =Row(name='Ravindra',salary='2000')
print(row1.name,row1.salary)

data= [row,row1]
df =spark.createDataFrame(data)
df.show()
df.printSchema()

data =[Row(name="Ravindra",prop=Row(hair="black",eye="blue")),\
       Row(name="Reddy",prop=Row(hair="brown",eye="brown"))]
df3 =spark.createDataFrame(data)
df3.show()
df3.printSchema()