from pathlib import Path
import shutil

# Xác định thư mục gốc project
BASE_DIR = Path(__file__).resolve().parent.parent

# Thư mục nguồn và đích
LANDING_DIR = BASE_DIR / "data" / "landing"
BRONZE_DIR = BASE_DIR / "lake" / "bronze" / "olist"


def main():
    if not LANDING_DIR.exists():
        print(f"[ERROR] Không tìm thấy thư mục nguồn: {LANDING_DIR}")
        return

    # Tìm tất cả file CSV trong data/landing
    csv_files = list(LANDING_DIR.glob("*.csv"))

    if not csv_files:
        print(f"[WARNING] Không có file CSV nào trong: {LANDING_DIR}")
        return

    copied_count = 0

    for csv_file in csv_files:
        # Tên bảng = tên file không có .csv
        table_name = csv_file.stem

        # Tạo thư mục bronze theo từng bảng
        target_table_dir = BRONZE_DIR / table_name
        target_table_dir.mkdir(parents=True, exist_ok=True)

        # Copy file vào bronze
        target_file = target_table_dir / csv_file.name
        shutil.copy2(csv_file, target_file)

        print(f"[OK] Copied: {csv_file.name} -> {target_file}")
        copied_count += 1

    print(f"\nHoàn tất. Đã copy {copied_count} file CSV vào Bronze.")


if __name__ == "__main__":
    main()
