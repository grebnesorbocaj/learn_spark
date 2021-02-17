from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile(f"{BaseConfig.DATA_FOLDER}/{BaseConfig.MOVIE_LENS_FOLDERS}/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
