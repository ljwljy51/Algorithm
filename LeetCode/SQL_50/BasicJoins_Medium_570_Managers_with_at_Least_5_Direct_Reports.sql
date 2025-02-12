--https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50
SELECT
    name
FROM
    Employee E1
    JOIN (
        SELECT
            managerId,
            count(*) AS directReports
        FROM
            Employee
        GROUP BY
            managerId
        HAVING
            count(*) >= 5
    ) E2 ON E1.id = E2.managerId