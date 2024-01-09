#1
SELECT 
    market_date,
    customer_id,
    vendor_id,
    product_id,
    quantity * cost_to_customer_per_qty AS price
FROM customer_purchases
WHERE product_id = 4 or product_id = 9;

#2
SELECT 
    market_date,
    customer_id,
    vendor_id,
    product_id,
    quantity * cost_to_customer_per_qty AS price
FROM customer_purchases
WHERE vendor_id >= 8 and vendor_id <= 10;

#--------------------------------------------------#

SELECT 
    market_date,
    customer_id,
    vendor_id,
    product_id,
    quantity * cost_to_customer_per_qty AS price
FROM customer_purchases
WHERE vendor_id BETWEEN 8 AND 10;

#3
#Since we need data from another table and there is no other field that would help us (without being redundant), 
#the only way to do this task is trough JOIN clause or some kind of subquery (in my opinion). 
#Assuming this, we simply do harmless changes in the WHERE clause of the subquery.

SELECT
    market_date,
    customer_id,
    vendor_id,
    quantity * cost_to_customer_per_qty price
FROM customer_purchases
WHERE market_date IN
    (
    SELECT market_date
    FROM farmers_market.market_date_info
    WHERE market_rain_flag = 0
    )
    LIMIT 5;

#--------------------------------------------------#

SELECT
    market_date,
    customer_id,
    vendor_id,
    quantity * cost_to_customer_per_qty price
FROM customer_purchases
WHERE market_date NOT IN
    (
    SELECT market_date
    FROM farmers_market.market_date_info
    WHERE market_rain_flag = 1
    )
    LIMIT 5;