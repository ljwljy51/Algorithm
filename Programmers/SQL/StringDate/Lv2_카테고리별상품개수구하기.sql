-- https://school.programmers.co.kr/learn/courses/30/lessons/131529
-- GROUP BY, ORDER BY에서는 별칭 사용 가능한 것에 주목
SELECT
    LEFT(PRODUCT_CODE, 2) AS CATEGORY,
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM
    PRODUCT
GROUP BY
    CATEGORY
ORDER BY
    CATEGORY