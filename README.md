# 🚀 Order-to-Delivery Analytics Pipeline

A **Data Engineering project** simulating an end-to-end data pipeline for analyzing **Order → Delivery** performance using the **[Olist E-Commerce Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**.

The project aims to design a modern data architecture that includes a **Data Lake (Bronze/Silver layers)**, **dbt for transformation**, **Airflow for orchestration**, and **Metabase for analytics visualization**.

---

## 🎯 Objectives

- Build a scalable **Data Lake** (Bronze → Silver → Data Warehouse)
- Standardize data transformation using **dbt**
- Automate and orchestrate ETL processes with **Apache Airflow**
- Visualize KPIs and business metrics using **Metabase / BI tools**

---

## 🏗️ System Architecture

Kaggle CSV files
↓
Data Lake (Bronze → Silver)
↓
Data Warehouse (PostgreSQL)
↓
dbt models (staging, marts, KPIs)
↓
Airflow DAGs (ETL orchestration)
↓
Metabase Dashboard (BI visualization)


---

## 📂 Repository Structure

ORDER_TO_DELIVERY_ANALYSTICS_PIPELINE/
│
├── airflow/
│ └── dags/ # Airflow DAGs for orchestration
│
├── bi/ # BI dashboards (Metabase, Power BI)
│
├── data/
│ └── landing/ # Raw CSV files from Kaggle
│
├── lake/
│ ├── bronze/olist/ # Bronze layer (raw zone)
│ └── silver/olist/ # Silver layer (cleaned, normalized)
│
├── db/
│ └── ddl/ # SQL scripts for schema and table creation
│
├── dbt/ # dbt project (models, marts, tests)
│
├── docs/ # Documentation and diagrams
│
├── scripts/ # Custom Python ETL scripts
│
├── requirements.txt # Python dependencies
├── dev-requirements.txt # Dev/test dependencies
├── .gitignore # Ignored local and system files
└── README.md # Project documentation


---

## ⚙️ Setup & Installation

### 🧩 Requirements
- Python **3.10+**
- PostgreSQL **15+** (Database: `ecommerce_dw`)
- Virtual environment tool (`venv` or `virtualenv`)
- Apache Airflow **2.10+**

---

### 🚀 Setup Steps

```bash
# 1️⃣ Clone the repository
git clone https://github.com/dilambestall/order-to-delivery-analytics.git
cd order-to-delivery-analytics

# 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 3️⃣ Install dependencies
pip install -r requirements.txt
pip install -r dev-requirements.txt

# 4️⃣ Create PostgreSQL database
createdb ecommerce_dw

🌬️ Run Airflow Locally
# 1️⃣ Set Airflow home (Linux/WSL)
export AIRFLOW_HOME=$(pwd)/airflow

# 2️⃣ Initialize the Airflow database
airflow db init

# 3️⃣ Create an admin user
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

# 4️⃣ Start Airflow webserver and scheduler
airflow webserver -p 8080
airflow scheduler

📊 Dataset
Source: Olist Brazilian E-Commerce Public Dataset

After downloading, extract all CSV files into:
data/landing/

🧠 Example DAGs

| DAG Name             | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| `hello_world_dag.py` | Simple test DAG to verify Airflow setup                                 |
| `etl_olist_daily.py` | ETL pipeline extracting Olist data and transforming into cleaned tables |

👥 Contributors

@dilambestall

@hovngnvm

🧾 License
This project is licensed under the MIT License.
See the LICENSE
 file for details.

 💡 Future Improvements
 Integrate CI/CD using GitHub Actions

Add dbt test coverage and documentation

Deploy Airflow with Docker Compose

Build interactive dashboards in Metabase
