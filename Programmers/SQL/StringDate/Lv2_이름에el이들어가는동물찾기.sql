-- https://school.programmers.co.kr/learn/courses/30/lessons/59047
-- 문제 꼼꼼히 읽기
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE
    ANIMAL_TYPE = "Dog"
    AND LOWER(NAME) LIKE "%el%"
ORDER BY
    NAME