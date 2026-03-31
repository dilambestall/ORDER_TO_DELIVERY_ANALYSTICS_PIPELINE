select
    oi.order_id,
    oi.order_item_id,
    o.customer_id,
    o.order_purchase_timestamp,
    oi.product_id,
    oi.seller_id,
    oi.price
from {{ ref('stg_order_items') }} oi
left join {{ ref('stg_orders') }} o
    on oi.order_id = o.order_id
