# Write your MySQL query statement below
WITH CTE1 AS (SELECT visited_on, SUM(amount) As total_amount
FROM
Customer
Group BY visited_on),


CTE2 AS
(
SELECT visited_on, SUM(total_amount) OVER ( ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
ROUND(AVG (total_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM
CTE1)

SELECT *
FROM CTE2
WHERE
visited_on >= (SELECT visited_on FROM CTE2 ORDER BY visited_on LIMIT 1) + 6
ORDER BY visited_on


