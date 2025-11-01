from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_olist_daily",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # chạy thủ công
    catchup=False,
    tags=["etl", "olist"]
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo '🔹 ETL Job Started...'"
    )

    extract = BashOperator(
        task_id="extract",
        bash_command="echo '📦 Extracting Olist data...'"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="echo '🧹 Transforming data into clean format...'"
    )

    load = BashOperator(
        task_id="load",
        bash_command="echo '🚀 Loading data into warehouse...'"
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo '✅ ETL Job Completed Successfully!'"
    )

    start >> extract >> transform >> load >> end
