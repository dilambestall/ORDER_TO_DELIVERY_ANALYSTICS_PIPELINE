select
    date_trunc('month', order_purchase_timestamp::timestamp) as month,
    count(distinct order_id) as total_orders,
    sum(price) as revenue,
    avg(price) as avg_order_value
from {{ ref('fact_order_items') }}
group by 1
order by 1
