from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
from learn_spark.utils.runner import run_local
from learn_spark.utils.sorting import sortedResults
import collections


def parseLine(line):
    fields = line.split(",")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)


def count_friends_by_age(sc):
    lines = sc.textFile(
        f"{BaseConfig.DATA_FOLDER}/{BaseConfig.FRIENDS_DATASET}/fakefriends.csv"
    )
    rdd = lines.map(parseLine)
    totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(
        lambda x, y: (x[0] + y[0], x[1] + y[1])
    )
    averagesByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])
    results = sortedResults(averagesByAge)

    print("age\t->\t# of friends")
    for key, value in results.items():
        print(f"{key}\t->\t{value}")


if __name__ == "__main__":
    sc = run_local("FriendsByAge")
    count_friends_by_age(sc)
