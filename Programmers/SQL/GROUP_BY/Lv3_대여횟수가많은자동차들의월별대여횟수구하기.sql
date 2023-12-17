-- https://school.programmers.co.kr/learn/courses/30/lessons/151139
-- 푸는데 진~~~~짜 헷갈렸다.
-- 서브쿼리 작동 방식, 조건 주는 방법 등에 유의
SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(HISTORY_ID) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    CAR_ID IN (
        SELECT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08'
            AND '2022-10'
        GROUP BY
            CAR_ID
        HAVING
            COUNT(HISTORY_ID) >= 5
    )
    AND DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08'
    AND '2022-10'
GROUP BY
    MONTH,
    CAR_ID
ORDER BY
    MONTH,
    CAR_ID DESC