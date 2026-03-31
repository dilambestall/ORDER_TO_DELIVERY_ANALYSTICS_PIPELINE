select distinct
    seller_id
from {{ source('olist', 'olist_sellers_dataset') }}
