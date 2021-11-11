import datetime
import numpy as np
import pandas as pd

import findspark
findspark.init()
findspark.find()


import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
#from pyspark.sql import SparkSession
#from pyspark import SparkContext




def init_spark():
  #spark = SparkSession.builder.getOrCreate()
  #sc = spark.sparkContext
  conf = SparkConf() \
         .setAppName('pandas_to_spark') \
         .setMaster('local') \
         .set("spark.cores.max", "52") \
         .set("spark.driver.memory", "52g") \
         .set("spark.driver.memoryOverhead", "52g") \
         .set("spark.executor.memory", "52g") \
         .set("spark.driver.memoryOverhead", "52g") \
         .set("spark.driver.maxResultSize", "0")
  sc = SparkContext(conf=conf)
  spark = SparkSession(sc)
  spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
  return spark,sc

def _map_to_pandas(rdds):
    return [pd.DataFrame(list(rdds))]

def toPandas(df, n_partitions=None):
    if n_partitions is not None: df = df.repartition(n_partitions)
    df_pand = df.rdd.mapPartitions(_map_to_pandas).collect()
    df_pand = pd.concat(df_pand)
    df_pand.columns = df.columns
    return df_pand




#298 GB
#n = 800000
#p = 50000

#2.38 GB
#n = 80000
#p = 4000

#medium
n = 100
p = 100


#small
#n = 1 
#p = 1

formatString = "\n\n\n------{0:-<80}"

print(formatString.format("generate pandas dataframe..."))
start_time = datetime.datetime.now()
pdf = pd.DataFrame(np.random.rand(n, p), columns=["x"+str(i+1) for i in range(p)])
end_time = datetime.datetime.now()
print(pdf)
print("------duration: {}------".format(end_time-start_time))

#print("\n\n\n---first line------------------------")
#print(pdf.head())

print(formatString.format("calculate pandas dataframe size..."))
from sys import getsizeof
start_time = datetime.datetime.now()
print(getsizeof(pdf)/(102410241024))
end_time = datetime.datetime.now()
print("------duration: {}------".format(end_time-start_time))

print(formatString.format("convert pandas dataframe to a spark dataframe..."))
spark,sc = init_spark()
start_time = datetime.datetime.now()
df = spark.createDataFrame(pdf)
end_time = datetime.datetime.now()
df.printSchema()
df.show()
print("------duration: {}------".format(end_time-start_time))

#convert a spark dataframe to local pandas dataframe throws error for data great than 2GB but goal is to convert 100 GB
print(formatString.format("convert spark dataframe to pandas dataframe..."))
start_time = datetime.datetime.now()
#pdf = df.toPandas()
pdf = toPandas(df, 1)
end_time = datetime.datetime.now()
print("------duration: {}------".format(end_time-start_time))
