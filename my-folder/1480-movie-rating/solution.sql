# Write your MySQL query statement below
(SELECT name AS results
FROM 
MovieRating mr
JOIN
Users u
ON
u.user_id = mr.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, name 
LIMIT 1
)
UNION ALL
(
SELECT title AS results
FROM 
MovieRating mr
JOIN
Movies m
ON
m.movie_id = mr.movie_id
WHERE MONTH(created_at) = 2 AND YEAR(created_at)= 2020
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1

)




