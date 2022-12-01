-- lists all records of the table `second_table` of the database `hbtn_0c_0`
-- only columns `score` and `name` (in this order)
-- only recordes with score >= 10
-- sorted by score (top first)
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;