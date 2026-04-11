from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

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

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /home/phuoc_di/order-to-delivery-analytics/dbt && \
        source /home/phuoc_di/odap_env/bin/activate && \
        dbt run
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /home/phuoc_di/order-to-delivery-analytics/dbt && \
        source /home/phuoc_di/odap_env/bin/activate && \
        dbt test
        """,
    )

    dbt_docs = BashOperator(
        task_id="dbt_docs_generate",
        bash_command="""
        cd /home/phuoc_di/order-to-delivery-analytics/dbt && \
        source /home/phuoc_di/odap_env/bin/activate && \
        dbt docs generate
        """,
    )

    end = BashOperator(
        task_id="end",
        bash_command='echo "ETL pipeline completed successfully"',
    )

    start >> dbt_run >> dbt_test >> dbt_docs >> end
