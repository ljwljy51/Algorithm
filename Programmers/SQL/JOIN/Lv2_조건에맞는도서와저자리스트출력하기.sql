-- https://school.programmers.co.kr/learn/courses/30/lessons/144854
SELECT
    BOOK_ID,
    AUTHOR_NAME,
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM
    BOOK AS A
    LEFT JOIN AUTHOR AS B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE
    CATEGORY = '경제'
ORDER BY
    PUBLISHED_DATE