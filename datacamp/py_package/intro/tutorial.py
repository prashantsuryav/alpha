# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np

# Create my_spark
spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(spark)

flight_dataframe = spark.read.format("csv").option("header", "true").load("spark-warehouse/flights_small.csv")
flight_dataframe.registerTempTable("flights")

# Print the tables in the catalog
print(spark.catalog.listTables())
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"
# Get the first 10 rows of flights
flights10 = spark.sql(query)
# Show the results
flights10.show()


# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"
# Run the query
flight_counts = spark.sql(query)
# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()
# Print the head of pd_counts
print(pd_counts.head())


# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))
# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)
# Examine the tables in the catalog
print(spark.catalog.listTables())
# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")
# Examine the tables in the catalog again
print(spark.catalog.listTables())

# Don't change this file path
file_path = "spark-warehouse/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()