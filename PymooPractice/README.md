\# NSGA-II Multi-Objective Optimization Practice



基于 Python 和 pymoo 的 NSGA-II 多目标优化实验项目。



\## 1. 项目介绍



本项目使用 NSGA-II 算法求解经典 ZDT1 双目标优化问题，研究不同迭代代数对算法性能的影响。



主要包括：



\- NSGA-II 算法求解 ZDT1

\- Pareto 前沿可视化

\- IGD 和 HV 性能评价

\- 不同迭代代数对比

\- 多随机种子重复实验

\- Wilcoxon 统计显著性检验



\## 2. 实验环境



\- Python 3.13.15

\- pymoo

\- NumPy

\- SciPy

\- Matplotlib



详细依赖版本见 `requirements.txt`。



\## 3. 主要文件



| 文件 | 作用 |

|---|---|

| nsga2\_zdt1.py | NSGA-II 求解 ZDT1 |

| plot\_pareto.py | 绘制理论与实验 Pareto 前沿 |

| evaluate\_nsga2.py | 计算 IGD、HV |

| compare\_generations.py | 比较不同迭代代数 |

| plot\_comparison.py | 绘制指标对比图 |

| multi\_seed\_experiment.py | 多随机种子重复实验 |

| wilcoxon\_test.py | 统计显著性检验 |

| experiment\_report.md | 实验报告 |



\## 4. 环境安装



在项目目录中执行：



```cmd

python -m venv .venv

.venv\\Scripts\\activate

python -m pip install -r requirements.txt

```



\## 5. 运行实验



按以下顺序执行：



```cmd

python nsga2\_zdt1.py

python plot\_pareto.py

python evaluate\_nsga2.py

python compare\_generations.py

python plot\_comparison.py

python multi\_seed\_experiment.py

python wilcoxon\_test.py

```



\## 6. 实验结果



ZDT1 测试问题，种群规模 100，每组使用 10 个随机种子。



| 迭代代数 | IGD Mean ± Std | HV Mean ± Std |

|---|---|---|

| 50 | 0.135336 ± 0.035511 | 0.661293 ± 0.052420 |

| 100 | 0.016635 ± 0.002491 | 0.847596 ± 0.004120 |

| 200 | 0.005268 ± 0.000316 | 0.868118 ± 0.000489 |



200 代与 100 代的配对 Wilcoxon 双侧检验结果：



\- IGD：p = 0.001953

\- HV：p = 0.001953



使用 Bonferroni 校正后的单项显著性阈值 0.025，两个指标均呈现统计显著差异。



需要注意，当前结果比较的是不同计算预算下的同一种算法，不能直接证明算法创新有效。



\## 7. 后续研究



\- 增加 ZDT2、ZDT3 等测试问题

\- 使用统一函数评价次数进行公平比较

\- 比较 NSGA-II 与 MOEA/D

\- 增加运行时间与计算成本分析

\- 开展多目标优化算法改进研究



\## 8. 说明



本项目用于多目标优化算法学习、科研实验流程训练与算法复现实践。

