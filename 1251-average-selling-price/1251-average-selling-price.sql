# Write your MySQL query statement below
Select p.product_id,
        COALESCE(ROUND(sum(p.price*s.units)/(sum(s.units)),2),0) as average_price
from Prices p LEFT JOIN UnitsSold s
on p.product_id = s.product_id
and s.purchase_date between p.start_date and p.end_date
GROUP BY 1