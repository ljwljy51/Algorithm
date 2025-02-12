--https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50
WITH recent_price AS (
    SELECT
        product_id,
        new_price
    FROM
        Products
    WHERE
        (product_id, change_date) IN (
            SELECT
                product_id,
                max(change_date)
            FROM
                Products
            WHERE
                change_date <= '2019-08-16'
            GROUP BY
                product_id
        )
)
SELECT
    DISTINCT Products.product_id,
    IFNULL(recent_price.new_price, 10) AS price
FROM
    Products
    LEFT JOIN recent_price ON Products.product_id = recent_price.product_id