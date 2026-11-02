
import unittest
import tempfile
import io

from pathlib import Path
from contextlib import redirect_stdout

from read_csv import read_csv_preview


class TestCSVReader(unittest.TestCase):

    # 测试 1：正常读取 CSV
    def test_normal_read(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "test.csv"

            path.write_text(
                "id,name\n1,ZhangSan\n2,LiSi\n",
                encoding="utf-8"
            )

            output = io.StringIO()

            with redirect_stdout(output):
                read_csv_preview(path, limit=5)

            self.assertIn("ZhangSan", output.getvalue())
            self.assertIn("LiSi", output.getvalue())

    # 测试 2：跳过 CSV 空行
    def test_skip_empty_lines(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "test.csv"

            path.write_text(
                "id,name\n1,ZhangSan\n\n2,LiSi\n",
                encoding="utf-8"
            )

            output = io.StringIO()

            with redirect_stdout(output):
                read_csv_preview(path, limit=5)

            result = output.getvalue()

            self.assertIn("ZhangSan", result)
            self.assertIn("LiSi", result)
            self.assertNotIn("[]", result)

    # 测试 3：文件不存在
    def test_file_not_found(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "missing.csv"

            output = io.StringIO()

            with redirect_stdout(output):
                read_csv_preview(path)

            self.assertIn("找不到文件", output.getvalue())
     
    
    # 测试 4：限制实际数据记录数量（不包含表头）
    def test_limit_records(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "test.csv"

            path.write_text(
                "id,name\n"
                "1,Alice\n"
                "2,Bob\n"
                "3,Tom\n"
                "4,Jack\n"
                "5,Lily\n"
                "6,David\n",
                encoding="utf-8"
            )

            output = io.StringIO()

            with redirect_stdout(output):
                read_csv_preview(path, limit=3)

            result = output.getvalue()

            self.assertIn("Alice", result)
            self.assertIn("Bob", result)
            self.assertIn("Tom", result)

            self.assertNotIn("Jack", result)
            self.assertNotIn("Lily", result)

            self.assertIn("共展示 3 条数据记录", result)
     
    # 测试 5：空 CSV 文件
    def test_empty_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "empty.csv"

            path.write_text("", encoding="utf-8")

            output = io.StringIO()

            with redirect_stdout(output):
                read_csv_preview(path, limit=5)

            result = output.getvalue()

            self.assertIn("共展示 0 条数据记录", result)



if __name__ == "__main__":
    unittest.main()
