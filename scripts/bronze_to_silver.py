from pathlib import Path
import pandas as pd

# Thư mục gốc project
BASE_DIR = Path(__file__).resolve().parent.parent

# Bronze và Silver
BRONZE_DIR = BASE_DIR / "lake" / "bronze" / "olist"
SILVER_DIR = BASE_DIR / "lake" / "silver" / "olist"


def main():

    if not BRONZE_DIR.exists():
        print("Bronze directory không tồn tại")
        return

    tables = list(BRONZE_DIR.iterdir())

    total = 0

    for table in tables:

        if not table.is_dir():
            continue

        csv_files = list(table.glob("*.csv"))

        if not csv_files:
            continue

        csv_file = csv_files[0]

        print(f"Đang xử lý {csv_file.name}")

        df = pd.read_csv(csv_file)

        silver_table_dir = SILVER_DIR / table.name
        silver_table_dir.mkdir(parents=True, exist_ok=True)

        parquet_file = silver_table_dir / f"{table.name}.parquet"

        df.to_parquet(parquet_file, index=False)

        print(f"[OK] Saved -> {parquet_file}")

        total += 1

    print(f"\nHoàn tất. Đã convert {total} bảng sang Silver.")


if __name__ == "__main__":
    main()
