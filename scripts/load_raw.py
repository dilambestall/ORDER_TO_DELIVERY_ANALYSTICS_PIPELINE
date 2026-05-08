from pathlib import Path
import shutil

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Source and target directories
LANDING_DIR = BASE_DIR / "data" / "landing"
BRONZE_DIR = BASE_DIR / "lake" / "bronze" / "olist"


def main():
    if not LANDING_DIR.exists():
        print(f"[ERROR] Landing directory not found: {LANDING_DIR}")
        return

    # Find all CSV files in data/landing.
    csv_files = list(LANDING_DIR.glob("*.csv"))

    if not csv_files:
        print(f"[WARNING] No CSV files found in: {LANDING_DIR}")
        return

    copied_count = 0

    for csv_file in csv_files:
        # Table name is the CSV file name without extension.
        table_name = csv_file.stem

        # Create one Bronze directory per source table.
        target_table_dir = BRONZE_DIR / table_name
        target_table_dir.mkdir(parents=True, exist_ok=True)

        # Copy source file into Bronze.
        target_file = target_table_dir / csv_file.name
        shutil.copy2(csv_file, target_file)

        print(f"[OK] Copied: {csv_file.name} -> {target_file}")
        copied_count += 1

    print(f"\nDone. Copied {copied_count} CSV files into Bronze.")


if __name__ == "__main__":
    main()
