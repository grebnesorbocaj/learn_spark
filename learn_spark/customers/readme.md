## Sorting Spend by Customer

Add up all spendings records per customer and sort by total spending.

## What do?

```
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
```