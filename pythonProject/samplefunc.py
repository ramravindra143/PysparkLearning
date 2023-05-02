from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('pivot').getOrCreate()
data =[('ram',100),('raghu',200),('ravi',300),('rag',400)]
schema =['name','salary']

df=spark.createDataFrame(data,schema)
df.show()
#df.sample(fraction=0.1,seed=123).show()
##Collect should not be used in the large dataframe
list=df.collect()
print(list)
print(list[0][0])
##Transform function
def convertToUpper(df):
    return df.withColumn('name',upper(df.name))
def doubleTheSalary(df):
    return df.withColumn('salary',df.salary *2)

df1=df.transform(convertToUpper).transform(doubleTheSalary)
df1.show()

spark.stop()

