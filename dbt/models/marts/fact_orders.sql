select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp
from {{ ref('stg_orders') }}
