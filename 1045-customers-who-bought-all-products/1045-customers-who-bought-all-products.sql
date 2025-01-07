# Write your MySQL query statement below
Select customer_id
from Customer
group by customer_id
having count(DISTINCT product_key) = (Select COUNT(*) from Product)