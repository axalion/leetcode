# Write your MySQL query statement below

Select activity_date AS day,
    count(DISTINCT user_id) AS active_users 
from Activity
where activity_date between DATE_SUB('2019-07-27', INTERVAL 30 DAY) AND '2019-07-27'
group by activity_date
