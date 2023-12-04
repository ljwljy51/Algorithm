-- https://school.programmers.co.kr/learn/courses/30/lessons/131530
-- 나는 그냥 DIV하고 10000 곱해서 구했는데, CASE 문 쓴 사람들이 많았다!
SELECT
    (PRICE DIV 10000) * 10000 AS PRICE_GROUP,
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM
    PRODUCT
GROUP BY
    PRICE_GROUP
ORDER BY
    PRICE_GROUP