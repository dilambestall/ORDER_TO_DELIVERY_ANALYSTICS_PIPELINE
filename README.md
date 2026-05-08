# Order-to-Delivery Analytics Pipeline

## Project Overview

This project is a portfolio Data Engineering / Analytics Engineering project built around an order-to-delivery dataset.

The goal is to practice building a structured analytics pipeline using Python, PostgreSQL, dbt, Airflow, GitHub Actions, and BI-ready datasets.

At the current stage, the project focuses on:

* Organizing order-to-delivery data in a clear project structure
* Loading cleaned data into PostgreSQL
* Building dbt staging and mart models
* Creating KPI-ready SQL models for analytics
* Running dbt validation through GitHub Actions
* Preparing cleaned datasets for BI/dashboard development

---

## Business Objective

The project aims to answer key business questions related to order and delivery performance, such as:

* How many orders were placed?
* How does revenue change over time?
* What is the average order value?
* Which customer segments or regions contribute most to sales?
* How can order-to-delivery data be prepared for dashboard reporting?

---

## Current Architecture

```text
Source CSV Data
        ↓
Cleaned / Prepared Data Files
        ↓
PostgreSQL Database
        ↓
dbt Models
        ↓
Staging Models
        ↓
Mart / KPI Models
        ↓
BI-ready Data Outputs
```

---

## Technologies Used

| Category                | Technology              |
| ----------------------- | ----------------------- |
| Programming             | Python                  |
| Database                | PostgreSQL              |
| Transformation          | dbt Core                |
| Orchestration           | Apache Airflow          |
| BI Preparation          | CSV / BI-ready datasets |
| Version Control         | Git + GitHub            |
| CI/CD                   | GitHub Actions          |
| Development Environment | WSL Ubuntu, VS Code     |

---

## Project Structure

```text
order-to-delivery-analytics-pipeline/
│
├── .github/
│   └── workflows/
│       └── dbt-ci.yml
│
├── airflow/
│   └── dags/
│
├── bi/
│   └── cleaned_data/
│
├── data/
│
├── db/
│   └── ddl/
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── dbt_project.yml
│   └── packages.yml
│
├── docs/
│
├── lake/
│
├── scripts/
│
├── README.md
└── requirements.txt
```

---

## Data Processing Layer

The project includes Python scripts for preparing and loading data into the database.

Current focus:

* Read source CSV files
* Clean and standardize selected datasets
* Load prepared data into PostgreSQL
* Store cleaned data outputs for later analytics and BI usage

---

## dbt Transformation Layer

dbt is used to transform database tables into analytics-ready models.

Current dbt layers:

| Layer   | Purpose                                | Example Pattern   |
| ------- | -------------------------------------- | ----------------- |
| Staging | Clean and standardize source tables    | stg_*             |
| Marts   | Build business-ready analytical models | customer_*, kpi_* |

The current KPI model is stored under:

```text
dbt/models/marts/
```

---

## Data Quality Checks

The project includes dbt tests to improve data reliability.

Current tests include:

* not_null
* unique
* dbt_utils.unique_combination_of_columns

These tests help validate important identifiers and prevent duplicate records in analytical models.

---

## Airflow Orchestration

Apache Airflow is included to practice workflow orchestration.

At the current stage, the Airflow DAG is used mainly to trigger dbt-related tasks.

This keeps the project closer to a real Data Engineering workflow where transformations are scheduled and monitored instead of being run manually.

---

## CI/CD with GitHub Actions

GitHub Actions is used to validate dbt changes automatically.

The current CI workflow includes dbt checks such as:

* Installing required dependencies
* Setting up the test environment
* Running dbt commands
* Validating dbt models and tests

This helps catch errors before changes are merged or pushed further.

---

## Analytics Output

The project prepares analytics-ready outputs that can be used for dashboard development.

Current analytical focus:

* Order metrics
* Revenue metrics
* Average order value
* Customer-related analysis
* Cleaned BI datasets

The `bi/cleaned_data/` folder stores prepared data outputs that can be connected to BI tools such as Metabase or Power BI.

---

## Key Learnings

This project demonstrates practical experience with:

* Building a structured data project repository
* Loading data into PostgreSQL
* Using dbt for staging and mart transformations
* Writing dbt tests for data quality
* Using Airflow for orchestration practice
* Setting up GitHub Actions for dbt CI
* Preparing data for business intelligence dashboards

---

## Project Status

In Progress

The project is being developed step by step, with the current focus on dbt transformations, data validation, orchestration practice, and BI-ready analytics outputs.
