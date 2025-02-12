--https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=top-sql-50
-- union 연산 주목
(
    SELECT
        "Low Salary" AS category,
        (
            SELECT
                count(*)
            FROM
                Accounts
            WHERE
                income < 20000
        ) AS accounts_count
)
UNION
ALL (
    SELECT
        "Average Salary" AS category,
        (
            SELECT
                count(*)
            FROM
                Accounts
            WHERE
                income >= 20000
                AND income <= 50000
        ) AS accounts_count
)
UNION
ALL (
    SELECT
        "High Salary" AS category,
        (
            SELECT
                count(*)
            FROM
                Accounts
            WHERE
                income > 50000
        ) AS accounts_count
)