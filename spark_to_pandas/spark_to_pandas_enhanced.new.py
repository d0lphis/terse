import sys, os, shutil, glob, datetime, math, gc, time
import numpy
import pandas



def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.2f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.2f}Yi{suffix}"

def prepare_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("{} cleaned.".format(path))
    os.makedirs(path)
    print("{} created.".format(path))



import findspark
findspark.init("/usr/wks/kode/gwksp/spark")
#findspark.find()

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession



blocks = 200
data_path = "/temp/dataframe"



def init_spark():
    #spark = SparkSession.builder.getOrCreate()
    #sc = spark.sparkContext
    conf = SparkConf() \
           .setAppName('pandas_to_spark') \
           .setMaster('local') \
           .set("spark.cores.max", "64") \
           .set("spark.driver.memory", "64g") \
           .set("spark.driver.memoryOverhead", "64g") \
           .set("spark.executor.memory", "64g") \
           .set("spark.driver.memoryOverhead", "64g") \
           .set("spark.driver.maxResultSize", "0") \
           .set("spark.sql.debug.maxToStringFields", "1000") \
           .set("spark.sql.execution.arrow.pyspark.enabled", "true") \
           .set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true") \
           .set("spark.sql.shuffle.partitions", blocks) \
           .set("spark.default.parallelism", blocks)
    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)
    #spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

    configurations = spark.sparkContext.getConf().getAll()
    for conf in configurations:
        print(conf)

    return spark,sc

def create_spark():
    spark = SparkSession.builder \
        .appName("pandas_to_spark") \
        .config("spark.cores.max", "64") \
        .config("spark.driver.memory", "64g") \
        .config("spark.driver.memoryOverhead", "64g") \
        .config("spark.executor.memory", "64g") \
        .config("spark.driver.memoryOverhead", "64g") \
        .config("spark.driver.maxResultSize", "0") \
        .config("spark.sql.debug.maxToStringFields", "1000") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .config("spark.sql.execution.arrow.pyspark.fallback.enabled", "true") \
        .config("spark.sql.shuffle.partitions", blocks) \
        .config("spark.default.parallelism", blocks) \
        .getOrCreate()

    configurations = spark.sparkContext.getConf().getAll()
    for conf in configurations:
        print(conf)

    return spark

def _map_to_pandas(rdds):
    return [pandas.DataFrame(list(rdds))]

def to_pandas(df, partition_number=None):
    if partition_number is not None: df = df.repartition(partition_number)
    df_pandas = df.rdd.mapPartitions(_map_to_pandas).collect()
    df_pandas = pandas.concat(df_pandas)
    df_pandas.columns = df.columns
    return df_pandas

def to_pandas_by_csv(df):
    #method 5: whole, write csv then read
    prepare_folder(data_path)
    df_path = data_path + "/spark_csv"
    df.write.format("csv").save(df_path)
    gc.collect()
    pdf = pandas.read_csv(glob.glob(r"" + df_path + "/*.csv")[0])

def to_pandas_by_parquet(df):
    #method 6: whole, write parquet then read
    prepare_folder(data_path)
    df_path = data_path + "/spark_parquet"
    df.write.parquet(df_path)
    gc.collect()
    #conda install fastparquet python-snappy
    pdf = pandas.read_parquet(glob.glob(r"" + df_path + "/*.parquet")[0], engine="fastparquet")

def slice_df(df, rows_per_time, partition_number):
    #df = df.repartition(partition_number)
    total_splits = df.count() / rows_per_time
    i = 0
    pdf_list = []
    prepare_folder(data_path)
    while i < total_splits:
        print("\n>>> getting slice {} ...".format(i))
        tmp_df = df.limit(rows_per_time)



        print("\n>>> cutting slice {} ...".format(i))
        df = df.subtract(tmp_df)
        #tmp_df.show(truncate=False)



        print("\n>>> converting slice {} ...".format(i))

        #method 1: slicing, original toPandas
        #pdf_list.append(tmp_df.toPandas())

        #method 2: slicing, optimized to_pandas
        #pdf_list.append(to_pandas(tmp_df, partition_number))

        #method 3: slicing, optimized to_pandas then write csv then read
        #pdf_path = data_path + '/pandas_csv_' + str(i)
        #pdf = to_pandas(tmp_df, partition_number)
        #pdf.to_csv(pdf_path, index=False, sep='\t', encoding='utf-8')
        #gc.collect()
        #pdf = pandas.read_csv(pdf_path)
        #pdf_list.append(pdf)

        #method 4: slicing, write csv then read
        df_path = data_path + "/spark_csv_" + str(i)
        tmp_df.write.format("csv").save(df_path)
        gc.collect()
        pdf = pandas.read_csv(glob.glob(r"" + df_path + "/*.csv")[0])
        pdf_list.append(pdf)

        i += 1
    print("\n>>> merging all converted slices ...")
    full_pdf = pandas.concat(pdf_list)
    full_pdf.info(memory_usage='deep')



n,p = 800000, 50000	#298 G
n,p = 800000, 20000	#119 G
n,p = 800000, 19000	#113 G
n,p = 800000, 18500	#110 G
n,p = 800000, 16800	#100 G
n,p = 800000, 15000	#89.41 G
n,p = 800000, 10000	#59.60 G
n,p = 800000, 5000	#29.80 G
n,p = 800000, 4000	#23.84 G
#n,p = 80000, 4000	#2.3841859251260757 G		
#n,p = 10000, 10000	#0.7450581938028336 G		0:12:20.452592
#n,p = 1000, 1000	#0.007450714707374573 G		0:00:02.895437

#n,p = 500, 500		#1.91 MB			0:02:12.425501

#n, p = 200, 200	#312.64 KB			0:00:41.727200
#n,p = 100, 100		#78.27 KB			0:00:10.255516
#n,p = 10,10		#944.00 B			0:00:17.168916
n,p = 1,1		#152.00 B			0:00:02.343219





formatString = "\n\n\n------{0:-<80}"

print(formatString.format("generate pandas dataframe..."))
start_time = datetime.datetime.now()
pdf = pandas.DataFrame(numpy.random.rand(n, p), columns=["x"+str(i+1) for i in range(p)])
end_time = datetime.datetime.now()
print(pdf)
print("------duration: {}------".format(end_time-start_time))



#print("\n\n\n---first line------------------------")
#print(pdf.head())



print(formatString.format("calculate pandas dataframe size..."))
from sys import getsizeof
start_time = datetime.datetime.now()
#print(str(getsizeof(pdf)/1024.0/1024.0/1024.0)+" GB")
print(sizeof_fmt(getsizeof(pdf)))
#print()
#print(pdf.memory_usage(index=True, deep=True).sum())
#print()
#print(pdf.info(memory_usage="deep"))
end_time = datetime.datetime.now()
print("------duration: {}------".format(end_time-start_time))



print(formatString.format("convert pandas dataframe to a spark dataframe..."))
spark,sc = init_spark()
start_time = datetime.datetime.now()
df = spark.createDataFrame(pdf)
end_time = datetime.datetime.now()
df.printSchema()
#df.show()
print("------duration: {}------".format(end_time-start_time))



rows_per_time = blocks
#partition_number = math.ceil(sys.getsizeof(df) / 102400)
partition_number = blocks
print("partition number: {}".format(partition_number))
#convert a spark dataframe to local pandas dataframe throws error for data great than 2GB but goal is to convert 100 GB
print(formatString.format("convert spark dataframe to pandas dataframe..."))
start_time = datetime.datetime.now()

#pdf = df.toPandas()

#pdf = to_pandas(df, partition_number)

pdf = to_pandas_by_csv(df)

#pdf = to_pandas_by_parquet(df)

#slice_df(df, rows_per_time, partition_number)


end_time = datetime.datetime.now()
print("------duration: {}------".format(end_time-start_time))
