--https://leetcode.com/problems/last-person-to-fit-in-the-bus/solutions/3634727/best-optimum-solution-with-explanation-using-joins/?envType=study-plan-v2&envId=top-sql-50
-- JOIN 연산 조건에 주목
-- 알고리즘적으로 접근
SELECT
    q1.person_name
FROM
    Queue q1
    JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY
    q1.turn
HAVING
    sum(q2.weight) <= 1000
ORDER BY
    sum(q2.weight) DESC
LIMIT
    1