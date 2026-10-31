

\# MyHashTable



\## 1. 项目介绍



本项目使用 C++17 实现一个基于链地址法（Separate Chaining）的哈希表。



哈希表采用 Key-Value 存储结构，通过哈希函数将 Key 映射到对应的桶（Bucket）。



当多个 Key 映射到同一个桶时，使用链表解决哈希冲突。



\## 2. 实现功能



\- 插入 Key-Value

\- 查找指定 Key

\- 更新重复 Key 的 Value

\- 删除指定 Key

\- 处理负数 Key

\- 处理哈希冲突

\- 自动扩容（Rehash）

\- 批量插入（insertMany）

\- 负载因子统计

\- 非法容量异常处理



\## 3. 项目结构



```text

MyHashTable/

├── include/

│   └── MyHashTable.h

├── src/

│   └── MyHashTable.cpp

├── tests/

│   ├── test.cpp

│   └── basic\_test.cpp

└── README.md

```



\## 4. 技术实现



\- C++17

\- vector

\- list

\- pair

\- unordered\_set

\- 异常处理

\- 移动语义



\## 5. 编译方法



在项目根目录执行：



```bash

g++ -std=c++17 -Wall -Wextra -I include tests/test.cpp src/MyHashTable.cpp -o test.exe

```



运行完整测试：



```bash

test.exe

```



编译基础测试：



```bash

g++ -std=c++17 -Wall -Wextra -I include tests/basic\_test.cpp src/MyHashTable.cpp -o basic\_test.exe

```



运行基础测试：



```bash

basic\_test.exe

```



\## 6. 时间复杂度



| 操作 | 平均时间复杂度 | 最坏时间复杂度 |

|---|---|---|

| insert | O(1) | O(n) |

| find | O(1) | O(n) |

| remove | O(1) | O(n) |

| rehash | O(n) | O(n) |



注：n 表示哈希表中的元素数量。平均复杂度基于哈希分布较均匀的假设。



\## 7. 测试情况



完整测试覆盖：



\- 非法容量

\- 空表

\- 重复 Key

\- 负数 Key

\- 哈希冲突

\- 删除操作

\- 自动扩容

\- 批量插入

\- 扩容后数据完整性



当前测试记录：29 项通过，0 项失败。


## 8. 性能测试

### 测试环境

- 编程语言：C++17
- 编译器：G++（MSYS2 UCRT64）
- 编译优化：-O2
- 数据规模：100,000 条
- 重复次数：5 次
- 计时工具：std::chrono::steady_clock

### 逐项插入与批量插入对比

| 测试轮次 | 逐项插入(ms) | 批量插入(ms) |
|---|---:|---:|
| 1 | 16.286 | 12.663 |
| 2 | 17.328 | 12.518 |
| 3 | 15.534 | 12.350 |
| 4 | 15.331 | 12.234 |
| 5 | 14.909 | 12.226 |
| 平均 | 15.878 | 12.398 |

### 实验结论

在本次 100,000 条数据的测试中：

- 逐项插入平均耗时：15.878 ms
- 批量插入平均耗时：12.398 ms
- 批量插入耗时降低约 21.914%
- 批量插入速度约为逐项插入的 1.281 倍

### 其他测试场景

- 4 条数据的小批次插入：3.800 μs
- 10,000 条重复 Key：最终元素数量为 1
- 已有 1,000 条数据后继续插入 1,000 条：最终元素数量为 2,000

注：以上结果仅代表当前测试环境和测试条件，
不代表所有数据规模和硬件环境下的性能表现。



