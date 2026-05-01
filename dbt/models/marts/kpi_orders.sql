with order_values as (
    select
        order_id,
        min(order_purchase_timestamp) as order_purchase_timestamp,
        sum(price) as order_value
    from {{ ref('fact_order_items') }}
    group by order_id
)

select
    date_trunc('month', order_purchase_timestamp) as month,
    count(order_id) as total_orders,
    sum(order_value) as revenue,
    sum(order_value) / count(order_id) as avg_order_value
from order_values
where order_purchase_timestamp >= '2017-01-01'
  and order_purchase_timestamp < '2018-08-01'
group by 1
order by 1
