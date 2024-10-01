# Write your MySQL query statement below
SELECT DISTINCT v.viewer_id AS id
FROM
Views v
WHERE 
author_id = viewer_id
ORDER BY id ASC

