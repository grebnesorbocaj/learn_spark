## Ratings Counter

This is the first running script, as part of Frank Kanes "Taming Big Data with Apache Spark and Python".

Code in directory: `learn_spark/ratings_counter/ratings-counter.py`

## What's Happening

The file is of some format where:
- each record is someone's rating of a movie
- the 3rd column is that rating

```
8   create rdd by taking data from u.data file, line by line. 
9   create rdd by modifying/creating a new rdd using only the 3rd field
10  create dictionary by running countByValue on result (counts the occurences of each value)
        output is (rating, number of occurences)
11  
12  sort by key (rating)
13  loop through and print
14
```