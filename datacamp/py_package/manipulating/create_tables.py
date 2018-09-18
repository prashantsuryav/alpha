from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# Create my_spark
spark = SparkSession.builder.getOrCreate()

flight_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/flights_small.csv")
flight_df.registerTempTable("flights")

# Create the DataFrame flights
flights = spark.table("flights")
# Show the head
print(flights.show())
# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time/60)


# Filter flights with a SQL string
long_flights1 = flights.filter("distance > 1000")
# Filter flights with a boolean column
long_flights2 = flights.filter(flights.distance > 1000)
# Examine the data to check they're equal
print(long_flights1.show())
print(long_flights2.show())


# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")
# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
# Define first filter
filterA = flights.origin == "SEA"
# Define second filter
filterB = flights.dest == "PDX"
# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)


# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")
# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")


flights = flights.withColumn("distance",  flights["distance"].cast("int"))
flights = flights.withColumn("air_time",  flights["air_time"].cast("int"))
# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()
# Find the longest flight from SEA in terms of duration
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()


# Average duration of Delta flights
flights.filter(flights.origin == "SEA").filter(flights.carrier == "DL").groupBy().avg("air_time").show()
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()


# Group by tailnum
by_plane = flights.groupBy("tailnum")
# Number of flights each plane made
by_plane.count().show()
# Group by origin
by_origin = flights.groupBy("origin")
# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()


flights = flights.withColumn("dep_delay",  flights["dep_delay"].cast("int"))
# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")
# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()
# Standard deviation
by_month_dest.agg(F.stddev("dep_delay")).show()


planes_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/planes.csv")
planes_df.registerTempTable("planes")
# Create the DataFrame flights
flights = spark.table("planes")


airports_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/airports.csv")
airports_df.registerTempTable("airports")
# Create the DataFrame flights
airports = spark.table("airports")


flights = spark.table("flights")

# Examine the data
print(airports.show())
# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")
# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")
# Examine the data again
print(flights_with_airports.show())
















