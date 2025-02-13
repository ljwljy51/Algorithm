--https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&envId=top-sql-50
SELECT
    round(sum(tiv_2016), 2) AS tiv_2016
FROM
    (
        SELECT
            *,
            count(*) over (PARTITION by tiv_2015) AS cnt1,
            count(*) over (PARTITION by lat, lon) AS cnt2
        FROM
            Insurance
    ) tmp
WHERE
    cnt1 >= 2
    AND cnt2 = 1