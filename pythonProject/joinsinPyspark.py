from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark =SparkSession.builder.master('local').appName('joins').getOrCreate()
data =[(1,'Ravindra'),(2,'Raghu'),(3,'Diwakar'),(4,'Prabhakar'),(5,'Surendra')]
data1=[(1,2000,'IT'),(2,40000,'IT'),(3,50000,'MKT'),(4,5000,'MEACH'),(6,5000,'MEACH')]

schema=['id','ename']
schema1=['id','salary','dept']

df= spark.createDataFrame(data,schema)
df1= spark.createDataFrame(data1,schema1)
df.show()
df1.show()
df.printSchema()
df1.printSchema()

df.join(df1, df.id ==df1.id,'inner').show()
df.join(df1, df.id ==df1.id,'left').show()
df.join(df1, df.id ==df1.id,'right').show()
df.join(df1, df.id ==df1.id,'full').show()
df.join(df1,df.id==df1.id,'leftsemi').show()
df.join(df1,df.id==df1.id,'leftanti').show()

#self join is pending
