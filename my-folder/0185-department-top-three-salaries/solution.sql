# Write your MySQL query statement below

WITH CTE AS(
SELECT e.id AS employeeid,e.name AS employeename,e.salary AS salary ,e.departmentId AS departmentid
, d.id AS ddid, d.name AS dname, DENSE_RANK() over(partition by d.name ORDER BY salary DESC) AS ranking
FROM
Employee e
JOIN
Department d
ON 
e.departmentId = d.id )

SELECT CTE.dname AS Department, cte.employeename AS Employee, cte.salary AS Salary
FROM CTE
WHERE 
ranking <= 3









