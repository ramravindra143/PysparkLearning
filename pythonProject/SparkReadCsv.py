from pyspark.sql import *
from pyspark.sql.types import *
spark = SparkSession.builder.master('local').appName('Sparkreadcsv').getOrCreate()
print(spark)

schema1 = StructType([StructField('Empid',IntegerType(),True),StructField('Ename',StringType(),True),StructField('Salary',DecimalType(),True),StructField('Grade',StringType(),True),StructField('Designanation',StringType(),True)])

df1=  spark.read.csv('C://Users//Dell//Desktop//data1//employees.csv',schema=schema1)
df1.show(10)
df1.printSchema()
df1.collect()

df2 = spark.read.format('csv').option('header',True).load('C://Users//Dell//Desktop//data1//employees1.csv')
df2.show()
help(spark.read.csv)

##If you wanted to read multiple csv file just provide the list of files as a list
#spark.read.csv(list)

##if you wanted to read a folder and csv files from it then use the foldername directlry
df3=spark.read.csv('C://Users//Dell//Desktop//data1//',header=True,inferSchema=True)
df3.printSchema()
df3.show()

##Ways to define a struct type
schema2 =StructType().add(field='empid',data_type=IntegerType())\
    .add(field='Ename',data_type=StringType())\
    .add(field='Salary',data_type=DecimalType())\
    .add(field='Designation',data_type=StringType())
df4 = spark.read.csv('C://Users//Dell//Desktop//data1//',header=True,inferSchema=True)
df4.show()
df4.printSchema()
