
# Python File I/O Practice

## 1. 项目简介

本项目是 Python 编程基础练习项目。

主要学习 CS50P 中的 File I/O、异常处理和模块化编程。

使用 Python 读取 CSV 文件，实现数据预览、空行处理、
异常捕获和自动化测试。

## 2. 项目功能

- 使用 open() 打开 CSV 文件
- 使用 with 自动关闭文件
- 使用 csv.reader() 解析 CSV 数据
- 自动跳过空行
- 单独显示 CSV 表头
- 支持指定读取的数据记录数量
- 处理文件不存在异常
- 处理字符编码异常
- 使用 unittest 进行自动化测试

## 3. 项目结构

```text
PythonFileIOPractice/
├── read_csv.py
├── students.csv
├── README.md
└── tests/
    └── test_read_csv.py
```

## 4. 运行环境

- Python 3.13
- Windows
- VS Code

本项目只使用 Python 标准库，
不需要额外安装第三方依赖。

## 5. 运行方法

进入项目文件夹：

```cmd
cd /d C:\Users\67474\learning-roadmap\PythonFileIOPractice
```

运行程序：

```cmd
python read_csv.py
```

## 6. CSV 数据格式

示例 students.csv：

```csv
id,name,math,python
1,ZhangSan,85,90
2,LiSi,92,88
3,WangWu,78,95
4,ZhaoLiu,90,93
5,ChenQi,88,91
```

程序会单独显示表头，并打印前五条有效数据。

## 7. 自动化测试

项目使用 Python unittest 测试框架。

测试内容：

1. 正常读取 CSV
2. 文件不存在异常
3. 跳过 CSV 空行
4. 限制读取数据数量
5. 空 CSV 文件处理

运行测试：

```cmd
python -m unittest discover -s tests -v
```

目标：5 项测试全部通过。

## 8. 学习知识点

- File I/O
- open()
- with
- csv.reader()
- try / except
- def 函数
- import 模块
- unittest 自动化测试

## 9. 后续改进方向

- 使用 pandas 处理 CSV
- 增加数据统计功能
- 使用 matplotlib 绘制实验曲线
- 读取多目标优化算法实验结果

## 10. 项目总结

通过本项目，掌握了 Python 文件读取、
CSV 解析、异常处理和自动化测试的基本方法。

为后续科研数据分析和多目标优化实验奠定基础。
