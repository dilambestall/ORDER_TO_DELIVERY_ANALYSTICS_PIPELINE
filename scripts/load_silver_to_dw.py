from pathlib import Path
import pandas as pd
import psycopg2

BASE_DIR = Path(__file__).resolve().parent.parent

SILVER_DIR = BASE_DIR / "lake" / "silver" / "olist"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "odap",
    "user": "postgres",
    "password": "postgres"
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

        columns_sql.append(f"{col} {col_type}")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS raw.{table_name} (
        {", ".join(columns_sql)}
    )
    """

    cur.execute(create_table_query)

    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))

    insert_query = f"""
        INSERT INTO raw.{table_name} ({columns})
        VALUES ({placeholders})
    """

    for row in df.itertuples(index=False):
        cur.execute(insert_query, tuple(row))

    conn.commit()
    cur.close()

def main():

    conn = psycopg2.connect(**DB_CONFIG)

    for dataset_dir in SILVER_DIR.iterdir():

        parquet_files = list(dataset_dir.glob("*.parquet"))

        if not parquet_files:
            continue

        parquet_file = parquet_files[0]
        table_name = dataset_dir.name

        print(f"Loading {table_name}...")

        load_table(parquet_file, table_name, conn)

    conn.close()

    print("Done loading Silver → Data Warehouse")

if __name__ == "__main__":
    main()
