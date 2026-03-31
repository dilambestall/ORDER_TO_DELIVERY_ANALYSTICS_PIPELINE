select distinct
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
from {{ source('olist', 'olist_customers_dataset') }}
