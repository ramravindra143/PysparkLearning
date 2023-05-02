from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('ArrayCode').getOrCreate()

data =[('ram',(1,2)),('ravindra',(3,4))]
schema =StructType([StructField('name',dataType=StringType()),\
                   StructField('number',dataType=ArrayType(IntegerType()))])

df1 =spark.createDataFrame(data=data,schema=schema)
df1.show()
df1.printSchema()
df1.withColumn('firstNumber',col('number')[0]).show()
df1.withColumn('secondNumber',col('number')[1]).show()

data1=[(1,2),(3,4)]
schema1=['num1','num2']
df3 =spark.createDataFrame(data1,schema1)
df3.show()
df3.printSchema()
df4 =df3.withColumn('numbers1',array(df3.num1,df3.num2))
df4.show()
df4.printSchema()

df5=df4.withColumn('haveit',array_contains(col('numbers1'),1))
df5.show()