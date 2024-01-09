#1
SELECT *
FROM vendor_booth_assignments AS vba
    LEFT JOIN vendor AS v
    ON v.vendor_id = vba.vendor_id
ORDER BY vendor_name, market_date;

#2
#Yes.
SELECT *
FROM customer_purchases AS cp
    LEFT JOIN customer AS c
        ON c.customer_id = cp.customer_id;

#3
SELECT *
FROM product_category AS pc
    INNER JOIN product AS p
        ON pc.product_category_id = p.product_category_id
    INNER JOIN vendor_inventory AS vi
        ON p.product_id = vi.product_id
WHERE pc.product_category_id = 1;