select distinct
    product_id,
    product_category_name
from {{ source('olist', 'olist_products_dataset') }}
