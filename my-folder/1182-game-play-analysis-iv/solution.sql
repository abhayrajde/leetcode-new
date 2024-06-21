# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id),2) AS fraction FROM 
(SELECT player_id,MIN(event_date) AS event_date FROM Activity GROUP BY player_id) a 
LEFT JOIN activity b
ON a.player_id = b.player_id 
AND b.event_date = DATE_ADD(a.event_date, INTERVAL 1 DAY)


