from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("testeCsv").getOrCreate()
df = spark.read.csv('sf-fire-calls.csv', header=True, inferSchema=True)
df.select("*").show()
