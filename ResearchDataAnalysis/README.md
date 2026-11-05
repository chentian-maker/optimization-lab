
# Research Data Analysis

## 项目介绍

使用 Pandas 和 Matplotlib 分析多目标优化算法的实验结果。

## 功能

1. 读取 CSV 实验数据
2. 查看 shape 和 dtype
3. 按算法分组统计
4. 计算 IGD、HV、Runtime 的均值和标准差
5. 导出 summary.csv
6. 自动生成三张 PNG 对比图

## 安装依赖

python -m pip install pandas matplotlib

## 运行方式

python analyze_result.py

## 数据说明

data/results.csv 包含教学模拟数据，
用于比较 NSGA-II 和 MOEA/D。

## 后续改进

- 支持更多优化算法
- 支持多种测试函数
- 支持 30 次独立运行
- 添加统计显著性检验
- 增加自动化测试

## 多算法科研实验数据分析（2026-11-05）

### 1. 实验目标

学习多目标优化算法的实验数据处理流程，包括：

- 模拟科研实验数据生成
- 数据清洗与异常检测
- 多算法、多测试函数统计
- IGD 与 HV 性能对比可视化
- Mean ± Std 实验表格生成
- 自动化结果检查

### 2. 实验设置

- 算法：NSGA-II、MOEA/D、NSGA-III
- 测试函数：DTLZ1、DTLZ2、DTLZ3
- 每组实验运行次数：10
- 原始记录：90
- 有效记录：87
- 异常记录：3

注意：本项目使用模拟数据，仅用于学习科研
数据分析流程，不代表真实算法性能。

### 3. 运行步骤

按顺序执行：

1. python generate_experiment_data.py
2. python clean_experiment_data.py
3. python plot_algorithm_comparison.py
4. python make_paper_table.py
5. python verify_experiment_outputs.py

### 4. 主要输出文件

- data/multi_algorithm_results.csv
  模拟实验原始数据

- output/clean_results.csv
  清洗后的有效记录

- output/invalid_results.csv
  检测到的异常记录

- output/algorithm_summary.csv
  各算法的均值与标准差

- output/igd_comparison.png
  IGD 性能对比图

- output/hv_comparison.png
  HV 性能对比图

- output/paper_table.csv
  实验结果统计表

- output/paper_table.md
  Markdown 格式的实验表格

### 5. 自动化测试

运行：

python verify_experiment_outputs.py

测试项目：
- 数据数量检查
- 数据清洗检查
- 统计表检查
- 科研图片文件检查
- Markdown 表格检查

测试结果：5 项全部通过。

### 6. 实验结论与局限

本次模拟数据中：

- NSGA-III 在三个测试函数上取得最低
  IGD 均值和最高 HV 均值。
- MOEA/D 的平均运行时间最短。
- 不同算法的标准差存在差异。

这些结果由预设的随机模拟参数产生，
不能作为真实算法优劣的科学证据。

后续计划：
1. 使用 pymoo 运行真实多目标优化算法
2. 计算真实 IGD、HV 指标
3. 开展多次独立运行与统计检验
4. 复现公开论文的实验结果
