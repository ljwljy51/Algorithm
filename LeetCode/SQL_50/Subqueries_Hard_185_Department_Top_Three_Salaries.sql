--https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50
WITH employee_department AS (
    SELECT
        D.name AS dept_name,
        salary,
        E.name AS emp_name,
        dense_rank() over (
            PARTITION by D.id
            ORDER BY
                salary DESC
        ) AS rnk
    FROM
        Employee E
        LEFT JOIN Department D ON E.departmentId = D.id
)
SELECT
    dept_name AS Department,
    emp_name AS Employee,
    salary AS Salary
FROM
    employee_department
WHERE
    rnk <= 3