#1
SELECT *
FROM customer;

#2
SELECT *
FROM customer
ORDER BY customer_last_name, customer_first_name
LIMIT 10;

#3
SELECT
	customer_id,
    customer_first_name
FROM customer
ORDER BY customer_first_name;