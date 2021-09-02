
SELECT date_trunc('week', created_at::date) AS weekly,
       SUM(distance), SUM(duration)          
FROM speed_userdata
GROUP BY weekly
ORDER BY weekly;
