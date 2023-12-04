-- https://school.programmers.co.kr/learn/courses/30/lessons/151138
-- Case문 사용법에 주목
-- 경과 날짜+1해줘야 함
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN "장기 대여"
        ELSE "단기 대여"
    END AS RENT_TYPE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE LIKE '2022-09-%'
ORDER BY
    HISTORY_ID DESC