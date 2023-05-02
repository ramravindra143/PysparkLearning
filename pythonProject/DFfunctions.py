from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark =SparkSession.builder.master('local').appName('functions').getOrCreate()
data=[('ravindra','IT','M',3000),('ravindra','IT','M',3000),('Ram','IT','M',10000),('Raghu','IT','M',1500),('brama','MKT','M',2000), \
      ('surendra','Store','M',2000),('Charan','Store','M',3000),('Satti','Sweeper','M',3000),('RaghuTdp','Cleaner','M',6000)]

schema =['ename','dept','gender','salary']


df =spark.createDataFrame(data,schema)
df1=df
df.show()
df.printSchema()
#df.dropDuplicates().show()
#df.distinct().show()
#df.dropDuplicates(['gender']).show()
df.sort(df.salary.asc()).show()
df.sort(df.salary.desc()).show()
df.orderBy(df.salary.desc()).show()
df.orderBy(df.salary.asc()).show()

df.union(df1).show()
df.unionAll(df1).show()

df.groupby(['dept']).count().show()
df.groupby(['dept']).sum('salary').show()
df.groupby(['dept']).min('salary').show()
df.groupby(['dept']).max('salary').show()

df.groupby(['dept']).agg(count('*').alias('countofEmps'),\
                         min('salary').alias('minSalary'),\
                         max('salary').alias('maxSalary'),\
                         sum('salary').alias('sumofSalary')).show()

