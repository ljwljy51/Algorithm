-- https://school.programmers.co.kr/learn/courses/30/lessons/132202
-- GROUP BY, ORDER BY, HAVING 절에서 별칭 쓸 때 '' 없이 써야함!!!!!!!!!!!!!!!!!!!
SELECT MCDP_CD AS '진료과코드', COUNT(APNT_YMD) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드