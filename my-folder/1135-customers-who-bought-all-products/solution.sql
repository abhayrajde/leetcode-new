# Write your MySQL query statement below
WITH CTE1 AS
(SELECT customer_id, COUNT(DISTINCT product_key) AS p1
FROM Customer
GROUP BY customer_id),

CTE2 AS
(
SELECT COUNT(DISTINCT product_key) AS p2
FROM 
Product)

SELECT customer_id FROM CTE1,CTE2
WHERE p1=p2 
