-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
SELECT
    ANIMAL_TYPE,
    COUNT(ANIMAL_ID) AS count
FROM
    ANIMAL_INS
WHERE
    ANIMAL_TYPE = 'Cat'
    OR ANIMAL_TYPE = 'Dog'
GROUP BY
    ANIMAL_TYPE
ORDER BY
    ANIMAL_TYPE