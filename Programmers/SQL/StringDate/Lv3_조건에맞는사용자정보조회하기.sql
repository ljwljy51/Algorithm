-- https://school.programmers.co.kr/learn/courses/30/lessons/164670
SELECT
    B.USER_ID,
    B.NICKNAME,
    CONCAT(
        B.CITY,
        ' ',
        B.STREET_ADDRESS1,
        ' ',
        B.STREET_ADDRESS2
    ) AS '전체주소',
    CONCAT(
        SUBSTRING(B.TLNO, 1, 3),
        '-',
        SUBSTRING(B.TLNO, 4, 4),
        '-',
        SUBSTRING(B.TLNO, 8, 4)
    ) AS '전화번호'
FROM
    USED_GOODS_BOARD AS A
    INNER JOIN USED_GOODS_USER AS B ON A.WRITER_ID = B.USER_ID
GROUP BY
    B.USER_ID
HAVING
    COUNT(BOARD_ID) >= 3
ORDER BY
    B.USER_ID DESC