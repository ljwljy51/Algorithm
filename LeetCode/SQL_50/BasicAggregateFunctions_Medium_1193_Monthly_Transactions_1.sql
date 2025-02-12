-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    substr(trans_date, 1, 7) AS MONTH,
    country,
    count(*) AS trans_count,
    sum(IF(state = 'approved', 1, 0)) AS approved_count,
    sum(amount) AS trans_total_amount,
    sum(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM
    Transactions
GROUP BY
    MONTH,
    country