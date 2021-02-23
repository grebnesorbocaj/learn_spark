import collections
import re


def sortedResults(rdd, by="key"):
    if by == "key":
        results = rdd.collect()
        return collections.OrderedDict(sorted(results))
    elif by == "intVal": 
        results = rdd.collect()
        valueKeySort = collections.OrderedDict(sorted(results, key=lambda x: int(x[1])))
        return valueKeySort

def cleanString(text: str):
    """
    Breaks up text based on words ('r/W+') with a unicode encoding
    :param text: string input variable
    :return:
    """
    return re.compile(pattern=r'/W+', flags=re.UNICODE).split(text.lower())
