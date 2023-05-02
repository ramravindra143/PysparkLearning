from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark =SparkSession.builder.master('local').appName('MapType').getOrCreate()
#spark.sparkContext.setLogLevel("INFO")
data = [('maheer',{'hair':'black','eye':'brown'}),('wafa',{'hair':'black','eye':'blue'})]
schema = StructType([StructField('name',StringType()),\
                     StructField('properties',dataType=MapType(StringType(),StringType()))])

df =spark.createDataFrame(data,schema)
df.show(truncate=False)
df.printSchema()

df1 = df.withColumn('hair',df.properties['hair'])
df2 = df.withColumn('eye',df.properties.getItem('eye'))
#df3 = df.withColumn('eye',df.properties.getKeys('eye'))
df1.show(truncate=False)
df2.show(truncate=False)

df4=df.select('name','properties',explode(df.properties))
df4.show()
df4.printSchema()



df5=df.withColumn('Keys',map_keys(df.properties))
df5.show(truncate=False)
df6 =df.withColumn('values',map_values(df.properties))
df6.show(truncate=False) 
