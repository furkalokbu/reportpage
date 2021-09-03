
DROP VIEW group_data_by_week_user;

CREATE OR REPLACE VIEW public.group_data_by_week_user AS
SELECT username, 
       SUM(distance) as sum_dist, 
       SUM(duration) as sum_dur, 
       AVG(distance/duration) as avg,
       date_trunc('week', date::date) AS weekly
FROM speed_userdata
JOIN users_customuser ON speed_userdata.user_id = users_customuser.id
GROUP BY username, weekly;



-- CREATE OR REPLACE VIEW public.group_data_by_week AS
-- SELECT date_trunc('week', date::date) AS weekly,
--        SUM(distance) as sum_dist, SUM(duration) as sum_dur, AVG(distance/duration) as avg      
-- FROM speed_userdata
-- GROUP BY weekly
-- ORDER BY weekly;


-- SELECT * FROM users_customuser;
