from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
from learn_spark.utils.runner import run_local
from learn_spark.utils.sorting import sortedResults
import collections


def parseLine(line):
    fields = line.split(",")
    stationId = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9 / 5) + 32
    return (stationId, entryType, temperature)


def min_temperatures(sc, maxTemp=False):
    lines = sc.textFile(f"{BaseConfig.DATA_FOLDER}/{BaseConfig.TEMP_1800S}/1800.csv")

    rdd = lines.map(parseLine)

    if maxTemp is True:
        temps = rdd.filter(lambda x: "TMAX" in x[1])
    else:
        temps = rdd.filter(lambda x: "TMIN" in x[1])

    stationTemps = temps.map(lambda x: (x[0], x[2]))

    if maxTemp is True:
        minOrMaxTemps = stationTemps.reduceByKey(lambda x, y: max(x, y))
    else:
        minOrMaxTemps = stationTemps.reduceByKey(lambda x, y: min(x, y))

    results = sortedResults(minOrMaxTemps)

    print(f"Location\t->\t{'Max' if maxTemp else 'Min'} Temps")
    for key, value in results.items():
        print(f"{key}\t->\t{value:.2f} F")


if __name__ == "__main__":
    sc = run_local("MinTemps")
    min_temperatures(sc, maxTemp=False)
