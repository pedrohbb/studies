#1
SELECT
    product_id,
    product_name,
    CASE
        WHEN product_qty_type = 'unit'
            THEN 'unit'
        ELSE 'bulk'
        END AS product_qty_type_condensed
FROM product
LIMIT 10;

#2
SELECT
    product_id,
    product_name,
    CASE
        WHEN product_qty_type = 'unit'
            THEN 'unit'
        ELSE 'bulk'
        END AS product_qty_type_condensed,
    CASE
        WHEN LOWER(product_name) LIKE '%pepper%'
            THEN 1
        ELSE 0
        END AS pepper_flag
FROM product
LIMIT 10;