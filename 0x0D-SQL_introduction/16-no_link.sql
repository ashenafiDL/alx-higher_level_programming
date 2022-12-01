-- lists all records of the table second_table of the database hbtn_0c_0
-- if name column is not NULL
SELECT
    score,
    name
FROM
    second_table
WHERE
    name != ""
ORDER BY
    score DESC;