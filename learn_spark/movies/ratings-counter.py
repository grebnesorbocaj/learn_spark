from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
from learn_spark.utils.runner import run_local
import collections


def ratings_counter(sc: SparkContext):
    lines = sc.textFile(
        f"{BaseConfig.DATA_FOLDER}/{BaseConfig.MOVIE_LENS_FOLDERS}/u.data"
    )
    ratings = lines.map(lambda x: x.split()[2])
    result = ratings.countByValue()

    sortedResults = collections.OrderedDict(sorted(result.items()))
    for key, value in sortedResults.items():
        print("%s %i" % (key, value))


if __name__ == "__main__":
    sc = run_local("RatingsHistogram")
    ratings_counter(sc)
