"""
count total amount spent by customer

use customer-orders.csv from data/cust-orders/ directory
    format of file:
        cust_id, item_id, amount_spent
    example of 5 lines:
        45, 140, 88.70
        51, 113, 51.50
        45, 151, 102.78
        31, 113, 51.50
        28, 201, 8.35

Want to ->
  filter to customer and price for each record
  reduceByKey adding up each purchase price
"""

from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
from learn_spark.utils.runner import run_local
from learn_spark.utils.sorting import sortedResults


def parseLine(line):
    fields = line.split(",")
    custId = int(fields[0])
    spent = float(fields[2])
    return (custId, spent)


def spending_per_customer(sc):
    lines = sc.textFile(
        f"{BaseConfig.DATA_FOLDER}/{BaseConfig.CONSUMER_SPENDING}/customer-orders.csv"
    )

    purchaseRecords = lines.map(parseLine)

    customerSpending = purchaseRecords.reduceByKey(lambda x, y: x + y)

    results = sortedResults(customerSpending, by="floatVal")

    print("word\t->\tcount")
    for custId, spending in results.items():
        print(f"{custId}  ->  ${spending:.2f}")


if __name__ == "__main__":
    sc = run_local("SpentByCustomer")
    spending_per_customer(sc)
