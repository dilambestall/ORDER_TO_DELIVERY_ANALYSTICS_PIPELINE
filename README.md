# 📦 Order-to-Delivery Analytics Pipeline

## 📌 Project Overview

This project is an end-to-end Data Engineering & Analytics pipeline built using modern data stack technologies.
The goal is to simulate a real-world retail/supply chain analytics system that processes order-to-delivery data and transforms it into business-ready KPIs and dashboards.

The project follows a layered architecture:

* Landing Layer
* Bronze Layer
* Silver Layer
* Data Warehouse Layer
* Analytics / BI Layer

The pipeline is orchestrated with Apache Airflow and transformed using dbt.

---

# 🧠 Business Objective

The project focuses on analyzing:

* Customer purchasing behavior
* Order processing performance
* Delivery efficiency
* Revenue trends
* Operational KPIs

The final output supports business intelligence dashboards for decision-making.

---

# 🏗️ Architecture

```text
Kaggle CSV Dataset
        ↓
Landing Layer
        ↓
Bronze Layer (Raw Data Lake)
        ↓
Silver Layer (Cleaned + Standardized Data)
        ↓
PostgreSQL Data Warehouse
        ↓
dbt Transformations
        ↓
Fact / Dimension Models
        ↓
KPI Models
        ↓
Metabase Dashboard
```

---

# ⚙️ Technologies Used

| Category        | Technology     |
| --------------- | -------------- |
| Programming     | Python         |
| Database        | PostgreSQL     |
| Transformation  | dbt Core       |
| Orchestration   | Apache Airflow |
| Visualization   | Metabase       |
| Data Storage    | CSV / Parquet  |
| Environment     | WSL Ubuntu     |
| Version Control | Git + GitHub   |
| CI/CD           | GitHub Actions |

---

# 📂 Project Structure

```text
order-to-delivery-analytics/
│
├── airflow/
│   └── dags/
│       └── etl_olist_daily.py
│
├── data/
│   └── landing/
│
├── lake/
│   ├── bronze/
│   └── silver/
│
├── db/
│   └── ddl/
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   └── kpi/
│   ├── tests/
│   └── macros/
│
├── docs/
│
├── scripts/
│   ├── load_raw.py
│   └── load_silver_to_dw.py
│
├── .github/
│   └── workflows/
│       └── dbt-ci.yml
│
├── requirements.txt
└── README.md
```

---

# 🥉 Bronze Layer

The Bronze layer stores raw data exactly as received from the source system.

Characteristics:

* Original CSV format
* No transformation
* Preserves source integrity
* Acts as historical backup

Example:

```text
/lake/bronze/olist_orders_dataset/
```

---

# 🥈 Silver Layer

The Silver layer standardizes and cleans raw data.

Processes include:

* Data type conversion
* Null handling
* Duplicate removal
* Standardized column naming
* Parquet conversion

Benefits:

* Faster querying
* Better storage efficiency
* Easier downstream transformations

---

# 🏢 Data Warehouse Design

The warehouse follows a dimensional modeling approach.

## Dimension Tables

* dim_customers
* dim_products
* dim_sellers
* dim_dates

## Fact Tables

* fact_orders
* fact_order_items
* fact_payments

---

# 🔄 dbt Transformation Layer

The dbt layer handles:

* Staging models
* Data quality tests
* Fact & dimension modeling
* KPI calculations
* Documentation generation

Naming convention:

| Layer     | Pattern |
| --------- | ------- |
| Staging   | stg_*   |
| Dimension | dim_*   |
| Fact      | fact_*  |
| KPI       | kpi_*   |

Example:

```text
stg_orders
fact_orders
kpi_orders
```

---

# ✅ dbt Tests

Implemented data quality tests include:

* unique
* not_null
* relationships
* accepted_values

Example:

```yaml
models:
  - name: dim_customers
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null
```

---

# ⏰ Airflow Orchestration

Apache Airflow is used to orchestrate the ETL pipeline.

Main DAG:

```text
etl_olist_daily
```

Pipeline tasks:

1. Load landing data
2. Move to Bronze layer
3. Transform to Silver layer
4. Load warehouse tables
5. Run dbt models
6. Run dbt tests

---

# 📊 KPI Dashboard

The BI dashboard focuses on:

## Sales KPIs

* Total Revenue
* Total Orders
* Average Order Value
* Monthly Revenue Trend

## Operational KPIs

* Delivery Time
* Late Delivery Rate
* Order Status Distribution

## Customer KPIs

* Repeat Customers
* Customer Segmentation
* Top Cities by Revenue

---

# 📈 Dashboard Features

The Metabase dashboard includes:

* KPI cards
* Revenue trend analysis
* Order trend analysis
* Donut charts
* Regional performance analysis
* Customer insights

---

# 🚀 CI/CD Pipeline

GitHub Actions is used for CI validation.

Current workflow:

```text
.github/workflows/dbt-ci.yml
```

CI checks:

* dbt dependency installation
* dbt debug
* dbt run
* dbt test

---

# 📚 Key Learnings

Through this project, the following concepts were practiced:

* End-to-end ETL pipeline development
* Data Lake architecture
* Dimensional modeling
* dbt transformation workflow
* Airflow orchestration
* Data quality testing
* CI/CD for data projects
* BI dashboard design
* Git & collaborative workflows

---

# ⭐ Project Status

✅ In Progress

The project is continuously updated with new pipeline features and dashboard improvements.
