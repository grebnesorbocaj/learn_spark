## Count Number of Friends by Ages

`spark-submit ratings-counter.py`

## What's Happening

I think the file is of some format where:
- each record is a friend
- id, name, age, number of friends he/she/they have
  - id, Bob, 31, 12 <- Bob is 31 and has 12 friends

```
16  create rdd of friends, line by line


19  create rdd taking only age and numFriends of each line
    9   split the line into fields by ','
    10  take the 3rd field as age
    11  take the 4th field as numFriends
    12  return age, numFriends
    
20  create rdd of total friends for each age
    mapValues(x: (x,1)) turns [age, numFriends] into [(age, numFriends), 1]
    reduceByKey(lambda x, y: x[0] + y[0], x[1] + y[1]) -> add by key (age) the number of friends and new field as counter
23  create rdd dividing numFriends by the counter (mapValues acts on values)
24  sort results by age

26  printing
27  for loop
28  printing
```