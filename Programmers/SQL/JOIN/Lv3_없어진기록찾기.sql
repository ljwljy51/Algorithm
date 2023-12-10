-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
SELECT
    A.ANIMAL_ID,
    A.NAME
FROM
    ANIMAL_OUTS AS A
    LEFT JOIN ANIMAL_INS AS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE
    INTAKE_CONDITION IS NULL