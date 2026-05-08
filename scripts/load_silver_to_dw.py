from pathlib import Path
import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
SILVER_DIR = BASE_DIR / "lake" / "silver" / "olist"

load_dotenv(BASE_DIR / ".env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "database": os.getenv("DB_NAME", "odap"),
    "user": os.getenv("DB_USER", "odap"),
    "password": os.getenv("DB_PASSWORD", "odap"),
}


def load_table(parquet_path, table_name, conn):
    df = pd.read_parquet(parquet_path)

    cur = conn.cursor()

    columns_sql = []

    for col, dtype in zip(df.columns, df.dtypes):
        if "int" in str(dtype):
            col_type = "BIGINT"
        elif "float" in str(dtype):
            col_type = "DOUBLE PRECISION"
        else:
            col_type = "TEXT"

        columns_sql.append(f'"{col}" {col_type}')

    create_table_query = f"""
    DROP TABLE IF EXISTS raw."{table_name}" CASCADE;

    CREATE TABLE raw."{table_name}" (
        {", ".join(columns_sql)}
    );
    """

    cur.execute(create_table_query)

    columns = ", ".join([f'"{col}"' for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    insert_query = f"""
        INSERT INTO raw."{table_name}" ({columns})
        VALUES ({placeholders})
    """

    for row in df.itertuples(index=False, name=None):
        cur.execute(insert_query, row)

    conn.commit()
    cur.close()


def main():
    conn = psycopg2.connect(**DB_CONFIG)

    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    conn.commit()
    cur.close()

    if not SILVER_DIR.exists():
        print(f"Silver directory does not exist: {SILVER_DIR}")
        conn.close()
        return

    for dataset_dir in SILVER_DIR.iterdir():
        if not dataset_dir.is_dir():
            continue

        parquet_files = list(dataset_dir.glob("*.parquet"))

        if not parquet_files:
            continue

        parquet_file = parquet_files[0]
        table_name = dataset_dir.name

        print(f"Loading raw.{table_name}...")
        load_table(parquet_file, table_name, conn)

    conn.close()
    print("Done loading Silver -> Postgres raw")


if __name__ == "__main__":
    main()
