--https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50
--결과 반환 부분에 주목
WITH prob_1_1 AS (
    SELECT
        user_id,
        count(*) AS rating_cnt
    FROM
        MovieRating
    GROUP BY
        user_id
),
prob_1_2 AS (
    SELECT
        name AS results
    FROM
        prob_1_1
        LEFT JOIN Users ON prob_1_1.user_id = Users.user_id
    WHERE
        rating_cnt =(
            SELECT
                max(rating_cnt)
            FROM
                prob_1_1
        )
    ORDER BY
        name
    LIMIT
        1
), prob_2_1 AS (
    SELECT
        movie_id,
        avg(rating) AS rating_avg
    FROM
        MovieRating
    WHERE
        substr(created_at, 1, 7) = '2020-02'
    GROUP BY
        movie_id
),
prob_2_2 AS (
    SELECT
        title AS results
    FROM
        prob_2_1
        LEFT JOIN Movies ON prob_2_1.movie_id = Movies.movie_id
    WHERE
        rating_avg =(
            SELECT
                max(rating_avg)
            FROM
                prob_2_1
        )
    ORDER BY
        title
    LIMIT
        1
)
SELECT
    *
FROM
    prob_1_2
UNION
ALL
SELECT
    *
FROM
    prob_2_2