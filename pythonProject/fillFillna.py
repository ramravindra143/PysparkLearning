from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('pivot').getOrCreate()
data =[(11,'Ravindra',None,10),(13,'Saritha','Female',10),(12,None,'Female',20),(14,'Damu','Male',20)]
schema =['id','name','gender','dept']
df=spark.createDataFrame(data,schema)
df.show()
#df.printSchema()
#df.fillna('unknown',['gender']).show()
df.na.fill('unknown',['gender']).show()