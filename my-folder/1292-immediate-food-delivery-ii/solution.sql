# Write your MySQL query statement below
SELECT
ROUND(SUM(CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END)*100/COUNT(customer_id),2) AS immediate_percentage
FROM Delivery
WHERE (order_date, customer_id) IN
(SELECT MIN(order_date) AS order_date, customer_id
FROM Delivery
GROUP BY customer_id)

