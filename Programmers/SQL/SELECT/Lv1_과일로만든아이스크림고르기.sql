-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
SELECT
    I.FLAVOR
FROM
    ICECREAM_INFO AS I
    INNER JOIN FIRST_HALF AS F ON I.FLAVOR = F.FLAVOR
WHERE
    F.TOTAL_ORDER > 3000
    AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    F.TOTAL_ORDER DESC