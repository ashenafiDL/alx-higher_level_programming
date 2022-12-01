-- lists all records of the table `second_table` of the database `hbtn_0c_0`
-- only columns `score` and `name` (in this order)
-- sorted by score (top first)
SELECT
    score,
    name
FROM
    second_table
ORDER BY
    score DESC;