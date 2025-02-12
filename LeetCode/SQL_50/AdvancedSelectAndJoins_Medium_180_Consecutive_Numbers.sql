--https://leetcode.com/problems/consecutive-numbers/?envType=study-plan-v2&envId=top-sql-50
-- 신박했던 문제.. 이렇게 테이블을 여러 개 병렬(?)로 참조해올 수 있다는 것엧 주목
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    LOGS l1,
    LOGS l2,
    LOGS l3
WHERE
    l1.Id = l2.Id -1
    AND l2.Id = l3.Id -1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num