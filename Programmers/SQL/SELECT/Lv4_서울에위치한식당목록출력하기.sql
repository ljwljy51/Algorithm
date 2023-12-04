-- https://school.programmers.co.kr/learn/courses/30/lessons/131118
-- 계산된 결과로 ORDER BY되는 것에 주목
-- NULL값을 갖는 결과 제외하기 위해 LEFT JOIN이 아닌 INNER JOIN을 해줌
-- 반올림 함수
-- join시 ambiguous하게 하지 않는 것에 주의
SELECT
    info.REST_ID,
    info.REST_NAME,
    info.FOOD_TYPE,
    info.FAVORITES,
    info.ADDRESS,
    ROUND(AVG(review.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_INFO AS info
    JOIN REST_REVIEW AS review ON info.REST_ID = review.REST_ID
GROUP BY
    info.REST_ID
HAVING
    ADDRESS LIKE '서울%'
ORDER BY
    SCORE DESC,
    info.FAVORITES DESC;