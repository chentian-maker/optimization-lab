
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
