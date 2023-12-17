-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 변수 선언 관련 부분 익히기
SET
    @HOUR = -1;

SELECT
    (@HOUR := @HOUR + 1) AS HOUR,
    (
        SELECT
            COUNT(*)
        FROM
            ANIMAL_OUTS
        WHERE
            HOUR(DATETIME) = @HOUR
    ) AS COUNT
FROM
    ANIMAL_OUTS
WHERE
    @HOUR < 23