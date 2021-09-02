

CREATE OR REPLACE VIEW public.group_data_by_week AS
SELECT date_trunc('week', date::date) AS weekly,
       SUM(distance) as sum_dist, SUM(duration) as sum_dur, AVG(distance/duration) as avg      
FROM speed_userdata
GROUP BY weekly
ORDER BY weekly;


