from pyspark import SparkConf, SparkContext
from learn_spark.config import BaseConfig
from learn_spark.utils.runner import run_local
from learn_spark.utils.sorting import cleanString, sortedResults


def count_words(sc):
    bookText = sc.textFile(f"{BaseConfig.DATA_FOLDER}/{BaseConfig.WORD_COUNT}/Book")

    words = bookText.flatMap(lambda x: x.split())

    wordCounts = words.countByValue()

    print("word\t->\tcount")
    for word, count in wordCounts.items():
        cleanWord = word.encode("ascii", "ignore")
        if cleanWord:
            print(f"{cleanWord.decode('ascii')}  ->  {count}")


def count_words_regex(sc):
    bookText = sc.textFile(f"{BaseConfig.DATA_FOLDER}/{BaseConfig.WORD_COUNT}/Book")

    words = bookText.flatMap(lambda sentence: sentence.split()).flatMap(
        cleanString
    )  # words is rdd

    # wordCounts = words.countByValue()
    wordCounts = sortByCount(words)  # wordCounts is rdd
    results = sortedResults(wordCounts, by="intVal")  # results is a python dict

    print("word\t->\tcount")
    for word, count in results.items():
        cleanWord = word.encode("ascii", "ignore")
        if cleanWord:
            print(f"{cleanWord.decode('ascii')}  ->  {count}")


def sortByCount(rdd):
    wordCounts = rdd.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    return wordCounts


if __name__ == "__main__":
    sc = run_local("WordCount")
    count_words_regex(sc)
