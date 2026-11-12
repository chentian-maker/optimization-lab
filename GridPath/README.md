# GridPath — 图搜索与网格路径规划实验

## 1. 项目介绍

GridPath 是一个基于 Python 的图搜索算法学习与实验项目。

项目以二维网格地图为基础，逐步实现广度优先搜索（BFS）、迭代深度优先搜索（DFS）和递归深度优先搜索，并通过多种地图场景对算法的正确性、最优性和运行效率进行比较。

## 2. 项目目标

- 理解队列、栈、递归和回溯机制。
- 掌握 BFS 和 DFS 的基本原理及代码实现。
- 理解搜索节点、展开节点和路径长度的区别。
- 比较不同搜索算法的性能。
- 验证算法能否找到合法路径以及是否保证最短路径。
- 使用 Pandas、Matplotlib 和 CSV 完成实验数据分析。

## 3. 项目结构

```text
GridPath/
│
├── grid_map.py
├── bfs.py
├── dfs.py
├── dfs_recursive.py
│
├── compare_search.py
├── plot_search_comparison.py
├── test_search_algorithms.py
│
├── comparison_results.csv
├── multi_map_test_results.csv
│
├── search_node_comparison.png
├── path_length_comparison.png
└── runtime_comparison.png
```

## 4. 算法介绍

### 4.1 BFS：广度优先搜索

核心数据结构：队列 deque。

搜索策略：先进先出（FIFO），逐层搜索。

特点：
- 能够找到可行路径。
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
- 代码结构直观，能够体现递归和回溯机制。
- 需要注意 Python 的递归深度限制。

时间复杂度：O(V + E)。

空间复杂度：O(V)，包含递归调用栈。

其中 V 表示节点数量，E 表示边数量。

## 5. 算法综合实验

实验地图：4×4 网格。

起点：(0, 0)。

终点：(3, 3)。

重复测试次数：1000。

最终实验结果：

| 指标 | BFS | 迭代 DFS | 递归 DFS |
|---|---:|---:|---:|
| 发现节点 | 13 | 13 | 13 |
| 展开节点 | 12 | 11 | 12 |
| 处理节点 | 13 | 12 | 13 |
| 路径长度 | 6 | 6 | 8 |
| 平均运行时间(ms) | 0.019225 | 0.017165 | 0.022861 |
| 理论保证最短 | 是 | 否 | 否 |
| 本次实际最短 | 是 | 是 | 否 |

说明：运行时间为本次小规模地图的单次测量结果，不代表算法在所有地图上的性能排序。

## 6. 多地图正确性测试

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

测试统计：

| 指标 | 结果 |
|---|---:|
| 测试场景 | 6 |
| 测试算法 | 3 |
| 总测试次数 | 18 |
| 通过次数 | 18 |
| 失败次数 | 0 |

测试通过率：100%。

注意：测试通过表示可达性判断正确，且找到的路径合法；DFS 不保证最短路径，因此最优性单独评价。

## 7. 实验数据与图表

实验数据：

- comparison_results.csv
- multi_map_test_results.csv

实验图表：

- search_node_comparison.png：节点数量对比。
- path_length_comparison.png：路径长度对比。
- runtime_comparison.png：运行时间对比。

## 8. 如何运行

安装依赖：

```bash
pip install pandas matplotlib numpy
```

运行 BFS：

```bash
python bfs.py
```

运行迭代 DFS：

```bash
python dfs.py
```

运行递归 DFS：

```bash
python dfs_recursive.py
```

运行综合实验：

```bash
python compare_search.py
```

生成对比图：

```bash
python plot_search_comparison.py
```

运行多地图测试：

```bash
python test_search_algorithms.py
```

## 9. 阶段总结

本阶段完成了 BFS、迭代 DFS 和递归 DFS 的实现，掌握了队列、栈、递归和回溯机制。

通过统一评价指标和多地图测试，理解了算法正确性、最优性和运行效率之间的区别。

下一阶段将继续学习带权图搜索算法，并逐步接触 Dijkstra 和 A*。

---

**项目阶段：W2 Day 4 完成**

**项目名称：GridPath**

**主要技术：Python、BFS、DFS、Pandas、Matplotlib、CSV**