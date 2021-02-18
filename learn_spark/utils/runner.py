from pyspark import SparkConf, SparkContext


def run_local(app_name):
    conf = SparkConf().setMaster("local").setAppName(f"{app_name}")
    return SparkContext(conf=conf)
