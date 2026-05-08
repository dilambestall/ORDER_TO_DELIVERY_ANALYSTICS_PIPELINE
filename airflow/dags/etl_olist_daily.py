from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = "/home/phuoc_di/order-to-delivery-analytics"
VENV_ACTIVATE = "/home/phuoc_di/odap_env/bin/activate"


def project_command(command: str) -> str:
    return f"cd {PROJECT_DIR} && source {VENV_ACTIVATE} && {command}"


with DAG(
    dag_id="etl_olist_daily",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "olist", "dbt"],
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command='echo "ETL pipeline started"',
    )

    load_raw = BashOperator(
        task_id="load_raw_to_bronze",
        bash_command=project_command("python scripts/load_raw.py"),
    )

    bronze_to_silver = BashOperator(
        task_id="bronze_to_silver",
        bash_command=project_command("python scripts/bronze_to_silver.py"),
    )

    load_silver_to_dw = BashOperator(
        task_id="load_silver_to_dw",
        bash_command=project_command("python scripts/load_silver_to_dw.py"),
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=project_command("cd dbt && dbt run"),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=project_command("cd dbt && dbt test"),
    )

    dbt_docs = BashOperator(
        task_id="dbt_docs_generate",
        bash_command=project_command("cd dbt && dbt docs generate"),
    )

    end = BashOperator(
        task_id="end",
        bash_command='echo "ETL pipeline completed successfully"',
    )

    (
        start
        >> load_raw
        >> bronze_to_silver
        >> load_silver_to_dw
        >> dbt_run
        >> dbt_test
        >> dbt_docs
        >> end
    )
