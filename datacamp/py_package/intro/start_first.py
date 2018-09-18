from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('MyFirstApp')
sc = SparkContext(conf=conf)

print(sc)
print(sc.version)