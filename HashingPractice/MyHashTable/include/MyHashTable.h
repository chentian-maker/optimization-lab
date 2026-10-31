
#pragma once

#include <vector>
#include <list>
#include <utility>

// MyHashTable：基于链地址法实现的哈希表
class MyHashTable {
private:
    // 哈希表的桶数量
    int capacity;

    // 每个桶使用链表保存 Key-Value
    std::vector<std::list<std::pair<int, int>>> table;

    // 当前哈希表中元素的数量
    int elementCount;

    // 检查初始化容量是否合法
    static int checkedCapacity(int size);

    // 将 Key 转换为合法的桶索引
    int hash(int key) const;

    // 判断指定 Key 是否存在
    bool containsKey(int key) const;

    // 扩容并重新分配元素
    void rehash(int newCapacity);

public:
    // 构造函数
    explicit MyHashTable(int size);

    // 获取当前元素数量
    int size() const;

    // 获取桶数量
    int bucketCount() const;

    // 获取负载因子
    double loadFactor() const;

    // 插入或更新 Key-Value
    void insert(int key, int value);

    // 批量插入 Key-Value
    void insertMany(
        const std::vector<std::pair<int, int>>& entries
    );

    // 查找 Key，将结果保存到 value 中
    bool find(int key, int& value) const;

    // 删除指定 Key
    bool remove(int key);

    // 显示哈希表内容
    void display() const;
};
