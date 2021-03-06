from pyspark.sql import SparkSession
import pyspark.ml.feature as features
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
import pyspark.ml.evaluation as evals
import pyspark.ml.tuning as tune
import numpy as np

if __name__ == "__main__":
    # Create my_spark
    spark = SparkSession.builder.appName("TuningApplication").getOrCreate()

    flight_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/flights_small.csv")
    flight_df.registerTempTable("flights")

    planes_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/planes.csv")
    planes_df.registerTempTable("planes")

    airports_df = spark.read.format("csv").option("header", "true").load("spark-warehouse/airports.csv")
    airports_df.registerTempTable("airports")

    # Create the DataFrame flights
    flights = spark.table("flights")
    planes = spark.table("planes")
    airports = spark.table("airports")

    # Rename year column
    planes = planes.withColumnRenamed("year", "plane_year")
    # Join the DataFrames
    model_data = flights.join(planes, on="tailnum", how="leftouter")

    # Cast the columns to integers
    model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
    model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
    model_data = model_data.withColumn("month", model_data.month.cast("integer"))
    model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

    # Create the column plane_age
    model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)

    model_data.show()
    # Create is_late
    model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)
    # Convert to an integer
    model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))
    # Remove missing values
    model_data = model_data.filter(
        "arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

    model_data.show()

    # Create a StringIndexer
    carr_indexer = features.StringIndexer(inputCol="carrier", outputCol="carrier_index")
    # Create a OneHotEncoder
    carr_encoder = features.OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")

    # Create a StringIndexer
    dest_indexer = features.StringIndexer(inputCol="dest", outputCol="dest_index")
    # Create a OneHotEncoder
    dest_encoder = features.OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")

    # Make a VectorAssembler
    vec_assembler = features.VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"],
                                             outputCol="features")

    # Make the pipeline
    flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])
    # Fit and transform the data
    piped_data = flights_pipe.fit(model_data).transform(model_data)
    # Split the data into training and test sets
    training, test = piped_data.randomSplit([.6, .4])

    # Create a LogisticRegression Estimator
    lr = LogisticRegression()
    # Create a BinaryClassificationEvaluator
    evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")

    # Create the parameter grid
    grid = tune.ParamGridBuilder()
    # Add the hyperparameter
    grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
    grid = grid.addGrid(lr.elasticNetParam, [0, 1])
    # Build the grid
    grid = grid.build()

    # Create the CrossValidator
    cv = tune.CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator)

    # # Fit cross validation models
    # models = cv.fit(training)
    # # Extract the best model
    # best_lr = models.bestModel
    # print(best_lr)

    # Call lr.fit()
    best_lr = lr.fit(training)
    # Print best_lr
    print(best_lr)

    # Use the model to predict the test set
    test_results = best_lr.transform(test)
    # Evaluate the predictions
    print(evaluator.evaluate(test_results))

spark.stop()