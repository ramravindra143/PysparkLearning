from pyspark.sql import SparkSession
from pyspark.sql.types import  *
from pyspark.sql.functions import *

spark = SparkSession.builder.master('local').appName('StuctType').getOrCreate()

#data =[(1,'Raghu'),(2,'Ram')]
data =[(1,('Raghu','Reddy')),(2,('Ram','Sita'))]
schema1 =StructType([StructField(name='FirstName',dataType=StringType()),StructField(name='LastName',dataType=StringType())])

schema=StructType([StructField(name='id',dataType=IntegerType()),\
                   StructField(name='name',dataType=schema1)])
#schema =['id','name']
#schema =StructType([StructField(name='id',dataType=IntegerType()),StructField(name='Ename',dataType=StringType())])
df1 =spark.createDataFrame(data=data,schema=schema)
df1.show()
df1.printSchema()