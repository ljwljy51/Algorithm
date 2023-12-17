-- https://school.programmers.co.kr/learn/courses/30/lessons/131123
-- 서브쿼리 사용해야 함!!
-- WHERE 조건 여러 칼럼 사용 시 묶어주기
SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM
    REST_INFO
WHERE
    (FOOD_TYPE, FAVORITES) IN(
        SELECT
            FOOD_TYPE,
            MAX(FAVORITES)
        FROM
            REST_INFO
        GROUP BY
            FOOD_TYPE
    )
ORDER BY
    FOOD_TYPE DESC