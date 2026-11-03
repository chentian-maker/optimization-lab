
# NumPyPractice

Python NumPy 基础学习与多目标优化入门项目。

## 1. 学习目标

- 掌握 NumPy 数组的创建
- 理解 shape、dtype、ndim
- 掌握索引和切片
- 使用 mean、std、min、max 计算统计量
- 理解 axis=0 和 axis=1
- 使用 NumPy 判断 Pareto 支配关系
- 使用 unittest 编写自动化测试

## 2. 项目文件

- numpy_basics.py：数组基本操作和统计分析
- optimization_stats.py：二维目标函数数组统计
- pareto_basics.py：Pareto 支配关系判断
- tests/test_pareto.py：自动化单元测试

## 3. 安装依赖

需要 Python 3 和 NumPy。

安装 NumPy：

python -m pip install numpy

## 4. 运行程序

基础数组练习：

python numpy_basics.py

多目标数据统计：

python optimization_stats.py

Pareto 支配测试：

python pareto_basics.py

## 5. 运行自动化测试

在 NumPyPractice 目录下执行：

python -m unittest discover -s tests -v

当前测试包含 7 个测试用例。

## 6. 核心知识

### shape

表示数组在各个维度上的大小。

例如：

shape=(5, 2)

表示 5 行、2 列。

### dtype

表示数组元素的数据类型。

例如：

int64：64 位整数
float64：64 位浮点数

### axis

axis=0：沿行方向计算，得到每列的统计量。
axis=1：沿列方向计算，得到每行的统计量。

### Pareto 支配

在所有目标都最小化的情况下：

如果方案 A 在每个目标上都不比 B 差，
并且至少有一个目标严格更优，
那么 A Pareto 支配 B。

## 7. 科研应用

本项目可作为后续多目标优化算法研究的基础。

未来可以进一步实现：

- Pareto 非支配解筛选
- 非支配排序
- NSGA-II
- 多目标优化结果可视化
