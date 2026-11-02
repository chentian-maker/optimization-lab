
import csv
from pathlib import Path



def read_csv_preview(path, limit=5):
    """读取 CSV 文件，展示表头和前 limit 条有效数据。"""

    count = 0

    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as file:

            reader = csv.reader(file)

            print("===== CSV 数据预览 =====")

            # 读取并单独展示表头
            header = next(reader, None)

            if header:
                print(f"表头: {header}")

            # 遍历实际数据
            for row in reader:

                # 跳过空行
                if not row:
                    continue

                # 达到指定数量后停止
                if count >= limit:
                    break

                count += 1

                print(f"第 {count} 条数据: {row}")

            print(f"\n共展示 {count} 条数据记录。")

    except FileNotFoundError:
        print(f"错误：找不到文件 {path}")

    except UnicodeError:
        print("错误：文件编码不正确。")

    except csv.Error as e:
        print(f"CSV 解析错误：{e}")


    except FileNotFoundError:
        print(f"错误：找不到文件 {path}")

    except UnicodeError:
        print("错误：文件编码不正确。")

    except csv.Error as e:
        print(f"CSV 解析错误：{e}")


if __name__ == "__main__":
    folder = Path(__file__).resolve().parent
    file_path = folder / "students.csv"

    read_csv_preview(file_path, limit=5)
