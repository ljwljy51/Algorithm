--https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    round(
        count(DISTINCT player_id) /(
            SELECT
                count(DISTINCT player_id)
            FROM
                Activity
        ),
        2
    ) AS fraction
FROM
    Activity
WHERE
    (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
        SELECT
            player_id,
            min(event_date)
        FROM
            Activity
        GROUP BY
            player_id
    )