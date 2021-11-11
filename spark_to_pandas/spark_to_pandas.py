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
  conf = pyspark.SparkConf().setAppName('pandas_to_spark').setMaster('local')
  sc = pyspark.SparkContext(conf=conf)
  spark = SparkSession(sc)
  return spark,sc



#298 GB
#n = 800000
#p = 50000

#2.38 GB
n = 80000
p = 4000

#small
#n = 1 
#p = 1


start_time = datetime.datetime.now()
pdf = pd.DataFrame(np.random.rand(n, p), columns=["x"+str(i+1) for i in range(p)])
end_time = datetime.datetime.now()
print("\n\n\n---pandas dataframe generated: {}------------------------".format(end_time-start_time))
print(pdf)

#print("\n\n\n---first line------------------------")
#print(pdf.head())

from sys import getsizeof
start_time = datetime.datetime.now()
print(getsizeof(pdf)/(102410241024))
end_time = datetime.datetime.now()
print("\n\n\n---pandas dataframe size: {}------------------------".format(end_time-start_time))

#convert local pandas dataframe to a spark dataframe
spark,sc = init_spark()
start_time = datetime.datetime.now()
df = spark.createDataFrame(pdf)
end_time = datetime.datetime.now()
print("\n\n\n---spark dataframe: {}------------------------".format(end_time-start_time))
df.printSchema()
df.show()

#convert a spark dataframe to local pandas dataframe throws error for data great than 2GB but goal is to convert 100 GB
start_time = datetime.datetime.now()
pdf = df.toPandas()
end_time = datetime.datetime.now()
print("\n\n\n---spark dataframe to pandas dataframe: {}------------------------".format(end_time-start_time))
