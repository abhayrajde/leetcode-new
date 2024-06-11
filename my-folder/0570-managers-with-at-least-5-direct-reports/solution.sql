# Write your MySQL query statement below
SELECT e1.name
FROM
Employee e1
LEFT JOIN 
Employee e2
ON
e1.id = e2.managerID
group by e2.managerId
HAVING COUNT(e2.id) >= "5"



