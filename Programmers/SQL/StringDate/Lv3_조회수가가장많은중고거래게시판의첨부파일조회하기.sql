-- https://school.programmers.co.kr/learn/courses/30/lessons/164671
SELECT
    CONCAT(
        '/home/grep/src/',
        B.BOARD_ID,
        '/',
        B.FILE_ID,
        B.FILE_NAME,
        B.FILE_EXT
    ) AS FILE_PATH
FROM
    USED_GOODS_BOARD AS A
    JOIN USED_GOODS_FILE AS B ON A.BOARD_ID = B.BOARD_ID
WHERE
    VIEWS =(
        SELECT
            MAX(VIEWS)
        FROM
            USED_GOODS_BOARD
    )
ORDER BY
    B.FILE_ID DESC