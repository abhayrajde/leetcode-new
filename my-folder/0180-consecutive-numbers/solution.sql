# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM
Logs l1
JOIN Logs l2
ON 
l1.id =l2.id-1 AND l2.num =l1.num
JOIN Logs l3
ON l1.id = l3.id-2 AND l3.num = l1.num


-- # LEAD LAG
-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM
-- (
-- SELECT
-- num,
-- LEAD(num) OVER (ORDER BY id)AS b4,
-- LAG(num) OVER (ORDER BY id) AS after
-- FROM Logs
-- ) a
-- WHERE 
-- num= b4 AND num=after




