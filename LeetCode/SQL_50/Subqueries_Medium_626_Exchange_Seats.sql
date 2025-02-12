--https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50
SELECT
    row_number() over() id,
    student
FROM
    Seat
ORDER BY
    IF (mod(id, 2) = 0, id -1, id + 1)