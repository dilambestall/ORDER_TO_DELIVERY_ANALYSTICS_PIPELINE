select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    price
from {{ source('olist', 'olist_order_items_dataset') }}
