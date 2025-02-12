--https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    customer_id
FROM
    Customer
GROUP BY
    customer_id
HAVING
    count(DISTINCT product_key) =(
        SELECT
            count(*)
        FROM
            Product
    )