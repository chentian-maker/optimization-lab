# GridPath — 图搜索算法与网格路径规划实验

## 1. 项目简介

GridPath 是一个基于 Python 的图搜索算法学习与实验项目。

项目以二维网格地图为基础，实现了三种经典图搜索算法：

- 广度优先搜索（BFS）
- 迭代深度优先搜索（Iterative DFS）
- 递归深度优先搜索（Recursive DFS）

通过不同地图场景，对算法的正确性、路径最优性、搜索节点数量和运行时间进行比较。

项目还实现了搜索过程记录、Matplotlib 可视化、分步搜索展示、统一算法接口和自动化测试。

## 2. 项目目标

- 理解队列、栈、递归和路径回溯机制。
- 掌握 BFS 和 DFS 的基本原理及代码实现。
- 理解搜索节点、展开节点、处理节点和路径长度的区别。
- 比较不同搜索算法的性能。
- 验证算法的可达性和最优性。
- 使用 Pandas、Matplotlib 和 CSV 完成实验数据分析。
- 掌握 Python 模块化设计和自动化测试。

## 3. 项目目录结构

```text
GridPath/
│
├── grid_map.py
├── bfs.py
├── dfs.py
├── dfs_recursive.py
│
├── visualize.py
├── compare_visualize.py
│
├── compare_search.py
├── plot_search_comparison.py
│
├── dijkstra.py
├── main.py
│
├── parent_practice.py
├── path_reconstruction.py
├── queue_practice.py
├── visited_practice.py
│
├── tests/
│   └── test_search_algorithms.py
│
├── comparison_results.csv
├── multi_map_test_results.csv
│
├── bfs_visualization.png
├── algorithm_comparison_visualization.png
├── bfs_steps/
│
├── search_node_comparison.png
├── path_length_comparison.png
├── runtime_comparison.png
│
└── README.md
```

## 4. 算法介绍

### 4.1 BFS：广度优先搜索

核心数据结构：队列 deque。

搜索策略：先进先出（FIFO），逐层搜索。

特点：

- 能够搜索可达节点。
- 在无权图中保证找到最短路径。
- 适合无权网格地图的最短路径搜索。

时间复杂度：O(V + E)。

空间复杂度：O(V)。

### 4.2 迭代 DFS：迭代深度优先搜索

核心数据结构：栈 list。

搜索策略：后进先出（LIFO），优先深入搜索。

特点：

- 能够搜索可达节点。
- 不保证找到最短路径。
- 可以通过显式栈管理搜索过程。

时间复杂度：O(V + E)。

空间复杂度：O(V)。

### 4.3 递归 DFS：递归深度优先搜索

核心机制：函数递归调用栈。

搜索策略：递归深入，搜索失败后返回上一层。

特点：

- 能够搜索可达节点。
- 不保证找到最短路径。
- 代码结构直观，能够体现递归与回溯机制。
- 需要注意 Python 的递归深度限制。

时间复杂度：O(V + E)。

空间复杂度：O(V)，包含访问记录和递归调用栈。

其中：
- V 表示节点数量。
- E 表示边数量。

## 5. 统一算法接口

三种算法均支持统一的调用参数：

```python
result = algorithm(
    grid,
    start,
    goal,
    return_details=True,
    verbose=False
)
```

详细模式下统一返回：

```python
{
    "path": path,
    "visited": visited,
    "search_log": search_log
}
```

字段说明：

| 字段 | 含义 |
|---|---|
| path | 最终搜索路径 |
| visited | 实际处理的节点顺序 |
| search_log | 搜索过程日志 |

当没有找到路径时，详细模式仍返回字典，其中 path 为 None。

默认模式则保持原有行为，只返回路径或 None。

## 6. 可视化功能

项目使用 Matplotlib 实现网格地图和搜索结果可视化。

### 6.1 最终路径可视化

运行 visualize.py，生成：

- bfs_visualization.png

颜色说明：

| 颜色 | 含义 |
|---|---|
| 白色 | 未搜索区域 |
| 灰色 | 障碍物 |
| 浅蓝色 | 已访问节点 |
| 红色 | 最终路径 |
| 绿色 | 起点 |
| 黄色 | 终点 |

### 6.2 BFS 分步可视化

程序根据 search_log 逐步生成搜索过程图片。

输出目录：

```text
bfs_steps/
├── bfs_step_01.png
├── bfs_step_02.png
├── ...
└── bfs_step_11.png
```

可以观察 BFS 每一步的搜索区域变化。

### 6.3 三种算法统一可视化

运行 compare_visualize.py，生成：

- algorithm_comparison_visualization.png

在相同地图、起点和终点条件下，对比：

- BFS
- Iterative DFS
- Recursive DFS

展示各算法的搜索区域、最终路径、路径长度和访问节点数量。

## 7. 算法综合实验

实验地图：4×4 网格。

起点：(0, 0)。

终点：(3, 3)。

重复测试次数：1000。

理论最短路径长度：6。

### 7.1 最新实验结果

| 指标 | BFS | 迭代 DFS | 递归 DFS |
|---|---:|---:|---:|
| 发现节点 | 13 | 13 | 13 |
| 展开节点 | 12 | 11 | 12 |
| 处理节点 | 13 | 12 | 13 |
| 路径长度 | 6 | 6 | 8 |
| 平均运行时间(ms) | 0.011353 | 0.010499 | 0.013388 |
| 理论保证最短 | 是 | 否 | 否 |
| 本次结果最短 | 是 | 是 | 否 |

说明：

1. BFS 在无权图中保证找到最短路径。
2. 迭代 DFS 本次找到最短路径，但不具有理论保证。
3. 递归 DFS 本次找到的路径长度为 8。
4. 运行时间为当前环境下的实验测量值，不代表所有地图上的性能排序。

注意：发现节点、处理节点和展开节点采用实验程序中的统计口径；与详细模式中的 visited 数量不应直接混为一谈。

## 8. 多地图正确性测试

测试场景：

1. 空旷地图。
2. 障碍地图。
3. 不连通地图。
4. 起点等于终点。
5. 终点不可通行。
6. 起点不可通行。

测试算法：

- BFS
- 迭代 DFS
- 递归 DFS

原有多地图实验记录：

| 指标 | 结果 |
|---|---:|
| 测试场景 | 6 |
| 测试算法 | 3 |
| 总测试次数 | 18 |
| 通过次数 | 18 |
| 失败次数 | 0 |

测试通过率：100%。

说明：路径可达性与路径最优性分别评价。DFS 不保证最短路径。

## 9. 自动化测试

测试文件：

```text
tests/test_search_algorithms.py
```

使用 Python unittest 框架。

测试内容：

| 测试项目 | 数量 |
|---|---:|
| BFS 路径搜索与最优性 | 2 |
| DFS 路径搜索 | 2 |
| 搜索日志一致性 | 3 |
| 非法起点和终点 | 2 |
| 不连通地图 | 1 |
| 总计 | 10 |

最新测试结果：

```text
Ran 10 tests

OK
```

10 项测试全部通过。

运行命令：

```bash
python -m unittest discover -s GridPath\tests -v
```

也可以单独运行：

```bash
python -m unittest GridPath.tests.test_search_algorithms -v
```

## 10. 实验数据与图表

实验数据：

- comparison_results.csv
- multi_map_test_results.csv

实验图表：

- search_node_comparison.png：节点数量对比。
- path_length_comparison.png：路径长度对比。
- runtime_comparison.png：运行时间对比。
- bfs_visualization.png：BFS 最终结果。
- algorithm_comparison_visualization.png：三算法可视化对比。

## 11. 环境配置

建议使用 Python 3.13 虚拟环境。

创建虚拟环境：

```bash
python -m venv .venv
```

激活环境：

```cmd
.venv\Scripts\activate
```

安装依赖：

```bash
python -m pip install matplotlib numpy pandas
```

## 12. 如何运行

在 learning-roadmap 项目根目录运行。

运行 BFS：

```bash
python GridPath\bfs.py
```

运行迭代 DFS：

```bash
python GridPath\dfs.py
```

运行递归 DFS：

```bash
python GridPath\dfs_recursive.py
```

运行 BFS 可视化：

```bash
python GridPath\visualize.py
```

运行三算法可视化：

```bash
python GridPath\compare_visualize.py
```

运行综合实验：

```bash
python GridPath\compare_search.py
```

生成实验对比图：

```bash
python GridPath\plot_search_comparison.py
```

运行自动化测试：

```bash
python -m unittest discover -s GridPath\tests -v
```

## 13. 阶段总结

本阶段完成了 BFS、迭代 DFS 和递归 DFS 的实现与实验。

掌握了：

- 队列和栈。
- BFS 和 DFS。
- 递归与回溯。
- 前驱节点和路径重建。
- 搜索过程日志。
- 统一算法接口。
- Matplotlib 网格可视化。
- 多地图实验。
- 自动化测试。
- 算法复杂度分析。

通过统一实验和可视化，理解了算法正确性、路径最优性、搜索工作量和运行时间之间的区别。

下一阶段计划学习带权图搜索算法，逐步进入 Dijkstra 和 A*，进一步完善路径规划项目。

---

**项目名称：** GridPath

**项目阶段：** W2 图搜索与路径规划

**主要技术：** Python、BFS、DFS、Matplotlib、CSV、unittest

**当前自动化测试：** 10/10 PASS
