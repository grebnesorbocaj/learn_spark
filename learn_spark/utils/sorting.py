from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
import collections


def sortedResults(rdd):
    results = rdd.collect()
    return collections.OrderedDict(sorted(results))
