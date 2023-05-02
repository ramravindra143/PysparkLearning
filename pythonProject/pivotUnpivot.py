from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('pivot').getOrCreate()
data =[(11,'Ravindra','Male',10),(13,'Saritha','Female',10),(12,'Manju','Female',20),(14,'Damu','Male',20)]
schema =['id','name','gender','dept']

df =spark.createDataFrame(data, schema)
pivotDF=df.groupby('dept').pivot('gender').count()
df.groupby('dept').pivot('gender',['Male']).count().show()


unPivotDF =pivotDF.select('dept',expr("stack(2,'M',Male,'F',Female) as (gender ,count)"))
unPivotDF.show()

