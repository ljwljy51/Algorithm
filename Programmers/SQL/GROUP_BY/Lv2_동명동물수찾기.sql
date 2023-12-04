-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
-- HAVING절에서 별칭 사용하는 것과, NULL값 처리하는 부분에 주의
SELECT
    NAME,
    COUNT(ANIMAL_ID) AS COUNT
FROM
    ANIMAL_INS
GROUP BY
    NAME
HAVING
    COUNT >= 2
    AND NAME IS NOT NULL
ORDER BY
    NAME