select
    order_id,
    customer_id,
    order_status,
    nullif(nullif(order_purchase_timestamp, ''), 'NaN')::timestamp
        as order_purchase_timestamp,
    nullif(nullif(order_approved_at, ''), 'NaN')::timestamp
        as order_approved_at,
    nullif(nullif(order_delivered_carrier_date, ''), 'NaN')::timestamp
        as order_delivered_carrier_date,
    nullif(nullif(order_delivered_customer_date, ''), 'NaN')::timestamp
        as order_delivered_customer_date,
    nullif(nullif(order_estimated_delivery_date, ''), 'NaN')::timestamp
        as order_estimated_delivery_date
from {{ source('olist', 'olist_orders_dataset') }}
