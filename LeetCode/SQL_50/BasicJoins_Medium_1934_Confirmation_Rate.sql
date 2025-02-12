--https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50
-- avg 함수 사용법에 유의
SELECT
    S.user_id,
    round(avg(IF(C.action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM
    Signups S
    LEFT JOIN (
        SELECT
            user_id,
            ACTION
        FROM
            Confirmations
    ) C ON S.user_id = C.user_id
GROUP BY
    S.user_id