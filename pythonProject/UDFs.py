from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark =SparkSession.builder.master('local').appName('udf').getOrCreate()
#def totalPay(s,b):
 #   return s +b

#@udf(returnType=IntegerType())
#def totalPay(s,b):
 #   return s +b
def emp(s,b):
    return s + b
data =((1,'Ram',2000,500),(2,'Ravi',2000,300))
schema =['id','name','salary','hike']

df =spark.createDataFrame(data,schema)
df.printSchema()
spark.udf.register(name='totalPay',f=emp,returnType=IntegerType())
#totalPayment=udf(lambda s,b:totalPay(s,b),IntegerType())
df.show()
df.createOrReplaceTempView('emp')
spark.sql('select id,name,salary,hike,totalPay(salary,hike)as totalSalary from emp').show()
#df1 =df.withColumn('TotaPay',totalPay(df.salary,df.hike))
#df1.show()
#df1.printSchema()

