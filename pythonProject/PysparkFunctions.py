from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import col,lit

spark = SparkSession.builder.master('local[4]').appName('PysparkFunctions').getOrCreate()

schema2 =StructType().add(field='empid',data_type=IntegerType())\
    .add(field='Ename',data_type=StringType())\
    .add(field='Salary',data_type=DecimalType())\
    .add(field='Designation',data_type=StringType())
df4 = spark.read.csv('C://Users//Dell//Desktop//data1//',header=True,inferSchema=True)
df4.show()
df4.printSchema()

df5 =df4.withColumn('new_Salary',df4.Salary+1000)
df5.show()
df5.printSchema()

##How to change the datatype using withColumn function
##While we are doing we have to make sure the cast function will take only datatypes is Integer,String,Date

df6=df5.withColumn(colName='new_Salary',col=col('new_Salary').cast('String'))
df6.show()
df6.printSchema()


##How to change the existing data using withColumn function
##if we use same column which is present in the existing dataframe then automatically it will make changes in existing column

df6 =df5.withColumn(colName='new_Salary',col=col('new_Salary') * 2)
df6.show()
df6.printSchema()

##How to create a new column with hard coded value
df7 =df6.withColumn('Country',lit('India'))
df7.show()
df7.printSchema()

##How to use existing column values as new column value
df8 =df7.withColumn('copied_Salary',col('new_Salary'))
df8.show()
df8.printSchema()