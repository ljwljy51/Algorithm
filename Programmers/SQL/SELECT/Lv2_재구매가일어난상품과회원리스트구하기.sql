--https://school.programmers.co.kr/learn/courses/30/lessons/131536
-- GROUP BY, HAVING 잘 이해하기!
SELECT
    USER_ID,
    PRODUCT_ID
FROM
    ONLINE_SALE -- USER_ID, PRODUCT_ID로 그룹화한 상태에서 PRODUCT_ID 개수가 두 개 이상인 경우
GROUP BY
    USER_ID,
    PRODUCT_ID
HAVING
    COUNT(PRODUCT_ID) > 1
ORDER BY
    USER_ID ASC,
    PRODUCT_ID DESC;