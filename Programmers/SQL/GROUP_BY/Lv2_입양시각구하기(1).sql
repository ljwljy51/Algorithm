-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
-- 별칭 사용 부분에 유의, 시간 추출 방법 주목
SELECT
    HOUR(DATETIME) AS HOUR,
    COUNT(ANIMAL_ID) AS COUNT
FROM
    ANIMAL_OUTS
GROUP BY
    HOUR
HAVING
    HOUR >= 9
    AND HOUR <= 19
ORDER BY
    HOUR