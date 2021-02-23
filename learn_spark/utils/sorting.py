import collections


def sortedResults(rdd):
    results = rdd.collect()
    return collections.OrderedDict(sorted(results))
