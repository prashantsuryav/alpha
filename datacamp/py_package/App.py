from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('MyFirstStandaloneApp')
sc = SparkContext(conf=conf)

userRDD = sc.textFile("C:/alpha/datacamp/py_package/resources/u.user")

def parse_N_calculate_age(data):
             userid,age,gender,occupation,zip = data.split("|")
             return  userid, age_group(int(age)),gender,occupation,zip,int(age)

def  age_group(age):
        if age < 10 :
           return '0-10'
        elif age < 20:
           return '10-20'
        elif age < 30:
           return '20-30'
        elif age < 40:
           return '30-40'
        elif age < 50:
           return '40-50'
        elif age < 60:
           return '50-60'
        elif age < 70:
           return '60-70'
        elif age < 80:
           return '70-80'
        else :
           return '80+'

data_with_age_bucket = userRDD.map(parse_N_calculate_age)

RDD_20_30 = data_with_age_bucket.filter(lambda line : '20-30' in line)

freq = RDD_20_30.map(lambda line : line[3]).countByValue()

print("total user count is ",userRDD.count())

print("total movie users profession wise ",dict(freq))

Under_age = sc.accumulator(0)
Over_age = sc.accumulator(0)

def outliers(data):
    global Over_age, Under_age
    age_grp = data[1]
    if(age_grp == "70-80"):
        Over_age +=1
    if(age_grp == "0-10"):
        Under_age +=1
    return data

df = data_with_age_bucket.map(outliers).collect()

print("under age users of the movie are ",Under_age)
print("over age users of the movie are ",Over_age)