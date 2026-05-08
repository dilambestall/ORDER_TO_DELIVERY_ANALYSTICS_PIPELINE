select
    date_trunc('month', order_purchase_timestamp) as month,
    count(*) as total_orders,
    count(order_delivered_customer_date) as delivered_orders,
    avg(
        date_part(
            'day',
            order_delivered_customer_date - order_purchase_timestamp
        )
    ) as avg_delivery_days,
    sum(
        case
            when order_delivered_customer_date > order_estimated_delivery_date
                then 1
            else 0
        end
    ) as late_deliveries,
    sum(
        case
            when order_delivered_customer_date > order_estimated_delivery_date
                then 1
            else 0
        end
    )::numeric / nullif(count(order_delivered_customer_date), 0) as late_delivery_rate
from {{ ref('stg_orders') }}
where order_purchase_timestamp >= '2017-01-01'
  and order_purchase_timestamp < '2018-08-01'
group by 1
order by 1
