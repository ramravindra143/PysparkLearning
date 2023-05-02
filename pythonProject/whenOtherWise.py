from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark =SparkSession.builder.master('local').appName('app').getOrCreate()
data =[('Ravindra','M',2000),('Raghu','F',3000),('Ramesh','',5000)]
schema =['name','gender','salary']
df =spark.createDataFrame(data,schema)
df.printSchema()
df.show()
df1 =df.select(df.name.alias('emp_name')\
               , df.salary.alias('emp_salary')\
               , when(df.gender == 'M', 'Male').when(df.gender == 'F', 'Female').otherwise('NULL').alias('emp_gender'))
df1.show()
df1.printSchema()

df1.sort(df1.emp_name.asc(),df1.emp_salary.desc(),df1.emp_gender).show()
df2=df1.select(df1.emp_name,df1.emp_salary.cast('int'),df1.emp_gender)
df2.show()
df1.show()
df1.printSchema()
df2.printSchema()

df2.filter(df2.emp_name.like('%a')).show()

df2.filter((df2.emp_name =='Ravindra') & (df2.emp_gender =='Male')).show()
df2.where((df2.emp_name =='Ravindra') & (df2.emp_gender =='Male')).show()