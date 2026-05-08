# Order-to-Delivery Analytics Pipeline

End-to-end analytics engineering project for the Olist Brazilian e-commerce dataset. The pipeline converts raw marketplace order data into curated warehouse models and BI-ready KPIs for revenue, customer segmentation, and delivery performance analysis.

## Highlights

- Layered data lake design: Landing -> Bronze -> Silver
- PostgreSQL warehouse with `raw`, `staging`, and `marts` schemas
- dbt transformation layer for staging views, dimensional marts, KPI tables, documentation, and tests
- Apache Airflow DAG for end-to-end orchestration
- CI workflow that validates the data pipeline and dbt project on GitHub Actions
- Power BI-ready output and exported analytical datasets

## Business Questions

The project is designed to support questions such as:

- How are orders, revenue, and average order value trending over time?
- Which customers are high-value, loyal, at-risk, or regular based on RFM behavior?
- How long does delivery take on average?
- What percentage of delivered orders arrive later than the estimated delivery date?
- Which customer, product, and seller dimensions support downstream BI analysis?

## Architecture

```text
Olist CSV Dataset
        |
        v
Landing Layer
        |
        v
Bronze Layer
Raw source files preserved by dataset
        |
        v
Silver Layer
Parquet files standardized for downstream loading
        |
        v
PostgreSQL Data Warehouse
raw -> staging -> marts
        |
        v
dbt Models and Tests
staging views, dimensions, facts, KPI marts
        |
        v
BI Outputs
Power BI report and exported analytical datasets
```

## Tech Stack

| Area | Technology |
| --- | --- |
| Data ingestion | Python |
| Data processing | pandas, pyarrow |
| Storage format | CSV, Parquet |
| Data warehouse | PostgreSQL |
| Transformation | dbt Core, dbt-postgres |
| Orchestration | Apache Airflow |
| BI | Power BI, exported CSV |
| CI/CD | GitHub Actions |

## Repository Structure

```text
.
|-- airflow/dags/              # Airflow orchestration
|-- bi/                        # Power BI report and BI-ready exports
|-- data/landing/              # Raw source files
|-- db/ddl/                    # Warehouse schema DDL
|-- dbt/models/staging/        # Source-aligned staging views
|-- dbt/models/marts/          # Dimensional, fact, KPI, and RFM models
|-- docs/                      # Supporting documentation
|-- lake/bronze/               # Raw lake layer
|-- lake/silver/               # Parquet lake layer
|-- scripts/                   # Python ETL scripts
|-- .github/workflows/         # CI/CD workflows
|-- requirements.txt
`-- README.md
```

## Data Pipeline

The pipeline is implemented as three Python ETL stages followed by dbt transformations:

```text
load_raw.py
  data/landing -> lake/bronze/olist

bronze_to_silver.py
  lake/bronze/olist -> lake/silver/olist

load_silver_to_dw.py
  lake/silver/olist -> PostgreSQL raw schema

dbt run + dbt test
  raw -> staging -> marts
```

Database credentials are read from a local `.env` file. A sanitized template is provided in `.env.example`; real credentials should never be committed.

## dbt Layer

dbt project: `order_to_delivery`

### Sources

The current dbt source layer reads from PostgreSQL schema `raw`:

- `olist_orders_dataset`
- `olist_order_items_dataset`
- `olist_customers_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`

### Staging Models

- `stg_orders`
- `stg_order_items`

### Mart Models

- `dim_customers`
- `dim_products`
- `dim_sellers`
- `fact_order_items`
- `customer_rfm`
- `kpi_orders`
- `kpi_delivery`

### KPI Outputs

`kpi_orders`

- monthly order count
- monthly revenue
- average order value

`kpi_delivery`

- monthly total orders
- delivered orders
- average delivery days
- late delivery count
- late delivery rate

`customer_rfm`

- recency
- frequency
- monetary value
- RFM score
- customer segment

## Data Quality

The dbt test suite validates core warehouse assumptions:

- non-null primary business keys
- uniqueness for dimension keys
- unique `(order_id, order_item_id)` combinations in `fact_order_items`
- non-null KPI fields for reporting tables

The project uses `dbt_utils` for advanced generic tests such as `unique_combination_of_columns`.

## Orchestration

Main DAG: `etl_olist_daily`

```text
start
  -> load_raw_to_bronze
  -> bronze_to_silver
  -> load_silver_to_dw
  -> dbt_run
  -> dbt_test
  -> dbt_docs_generate
  -> end
```

The DAG is configured for manual triggering, which keeps local development runs explicit and controlled.

## CI/CD

GitHub Actions workflows:

- `dbt-ci.yml`: provisions PostgreSQL, downloads source data, runs the Python ETL steps, executes `dbt run`, and validates `dbt test`
- `dbt-cd.yml`: validates dbt project parsing and compilation for deployment readiness

## BI Outputs

The BI layer includes:

- Power BI report: `bi/reports.pbix`
- exported customer RFM dataset
- exported monthly KPI dataset
- exported customer geography dataset

These outputs are designed for stakeholder-facing analysis of sales trends, customer segmentation, and delivery operations.

## Validation

The current pipeline has been validated locally with:

```text
Python ETL: passed
dbt compile: passed
dbt run: passed
dbt test: 24 passed, 0 failed
```

## Roadmap

- Add payments, reviews, and geolocation staging models
- Add `fact_orders`, `fact_payments`, and `dim_dates`
- Add relationship and accepted-value tests
- Optimize PostgreSQL loading with bulk insert or COPY
- Containerize the full local stack with Docker Compose

## License

This project is licensed under the MIT License.
