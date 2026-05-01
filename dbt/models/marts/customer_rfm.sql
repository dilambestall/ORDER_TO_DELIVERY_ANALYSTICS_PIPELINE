with max_date as (
    select
        max(order_purchase_timestamp) as max_order_date
    from {{ ref('fact_order_items') }}
),

order_values as (
    select
        dc.customer_unique_id,
        foi.order_id,
        min(foi.order_purchase_timestamp) as order_purchase_timestamp,
        sum(foi.price) as order_value
    from {{ ref('fact_order_items') }} foi
    join {{ ref('dim_customers') }} dc
        on foi.customer_id = dc.customer_id
    where foi.order_purchase_timestamp >= '2017-01-01'
      and foi.order_purchase_timestamp < '2018-08-01'
    group by
        dc.customer_unique_id,
        foi.order_id
),

rfm_base as (
    select
        ov.customer_unique_id,
        date_part(
            'day',
            md.max_order_date - max(ov.order_purchase_timestamp)
        ) as recency_days,
        count(distinct ov.order_id) as frequency,
        sum(ov.order_value) as monetary
    from order_values ov
    cross join max_date md
    group by
        ov.customer_unique_id,
        md.max_order_date
),

rfm_scores as (
    select
        customer_unique_id,
        recency_days,
        frequency,
        monetary,
        ntile(5) over (order by recency_days desc) as recency_score,
        ntile(5) over (order by frequency asc) as frequency_score,
        ntile(5) over (order by monetary asc) as monetary_score
    from rfm_base
)

select
    customer_unique_id,
    recency_days,
    frequency,
    monetary,
    recency_score,
    frequency_score,
    monetary_score,
    recency_score + frequency_score + monetary_score as rfm_total_score,

    case
        when recency_score >= 4
            and frequency_score >= 4
            and monetary_score >= 4
            then 'VIP'

        when recency_score >= 4
            and frequency_score >= 3
            then 'Loyal Customers'

        when recency_score >= 3
            and frequency_score >= 2
            then 'Potential Loyalists'

        when recency_score <= 2
            and frequency_score >= 3
            then 'At Risk'

        when monetary_score >= 4
            then 'High Value'

        else 'Regular'
    end as customer_segment
from rfm_scores
