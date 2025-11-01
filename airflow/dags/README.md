# airflow/dags

Thư mục chứa **DAGs** của Apache Airflow để orchestration ETL cho dự án.

## Quy ước gợi ý
- Tên DAG chính: `etl_olist_daily`
- Lịch chạy: `0 2 * * *` (2:00 sáng hằng ngày)
- Tags: `["olist","etl"]`
- Connections/Variables (ví dụ):
  - `POSTGRES_CONN_ID` – kết nối tới DW
  - `LAKE_ROOT` – đường dẫn Lake (`D:\order-to-delivery-analytics\lake`)

## Cấu trúc tham khảo
