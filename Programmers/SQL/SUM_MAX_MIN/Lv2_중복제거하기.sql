-- https://school.programmers.co.kr/learn/courses/30/lessons/59408

-- NULL값이 아닌 것 추출하는 것에 주의
-- DISTINCT 처음 써봄
SELECT COUNT(DISTINCT NAME) as count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL