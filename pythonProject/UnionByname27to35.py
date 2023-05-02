from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('function1').getOrCreate()

data =[('ravindra',123),('ram',124),('raghu',125),('raheem',126)]
data1 =[('ravindra',2000),('ram',3000),('raghu',4000),('raheem',5000)]
schema=['name','id']
schema1=['name','salary']
df=spark.createDataFrame(data,schema)
df1=spark.createDataFrame(data1,schema1)
#df.show()
#df1.show()
#df.printSchema()
#df1.printSchema()

#df.union(df1).show()
#df.unionAll(df1).show()
#df.unionByName(df1,allowMissingColumns=True).show()
df.select('id','name').show()
df.select(df['id'],df['name']).show()
df.select(df.id,df.name).show()


