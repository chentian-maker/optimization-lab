
#include "MyHashTable.h"

#include <iostream>
#include <stdexcept>
#include <limits>
#include <unordered_set>
#include <utility>

// ================================
// 私有成员函数
// ================================

// 检查初始化容量是否合法
int MyHashTable::checkedCapacity(int size) {
    if (size <= 0) {
        throw std::invalid_argument("Capacity must be positive.");
    }

    return size;
}

// 将 Key 转换为合法的桶索引
int MyHashTable::hash(int key) const {
    return ((key % capacity) + capacity) % capacity;
}

// 判断指定 Key 是否已经存在
bool MyHashTable::containsKey(int key) const {
    int index = hash(key);

    for (const auto& item : table[index]) {
        if (item.first == key) {
            return true;
        }
    }

    return false;
}

// 扩大桶的数量，并重新分配所有元素
void MyHashTable::rehash(int newCapacity) {
    auto oldTable = std::move(table);

    capacity = newCapacity;
    table.clear();
    table.resize(capacity);
    elementCount = 0;

    for (const auto& bucket : oldTable) {
        for (const auto& item : bucket) {
            int index = hash(item.first);
            table[index].push_front(item);
            ++elementCount;
        }
    }
}

// ================================
// 公有成员函数
// ================================

// 构造函数
MyHashTable::MyHashTable(int size)
    : capacity(checkedCapacity(size)),
      table(capacity),
      elementCount(0) {
}

// 获取当前元素数量
int MyHashTable::size() const {
    return elementCount;
}

// 获取桶数量
int MyHashTable::bucketCount() const {
    return capacity;
}

// 获取负载因子
double MyHashTable::loadFactor() const {
    return static_cast<double>(elementCount) / capacity;
}

// 插入或更新 Key-Value
void MyHashTable::insert(int key, int value) {
    int index = hash(key);

    // 如果 Key 已存在，直接更新 Value
    for (auto& item : table[index]) {
        if (item.first == key) {
            item.second = value;
            return;
        }
    }

    // 如果插入后负载因子超过 0.75，则扩容
    if (static_cast<double>(elementCount + 1) / capacity > 0.75) {
        if (capacity > std::numeric_limits<int>::max() / 2) {
            throw std::length_error("Hash table capacity is too large.");
        }

        rehash(capacity * 2);
        index = hash(key);
    }

    table[index].push_front({key, value});
    ++elementCount;
}

// 批量插入 Key-Value
void MyHashTable::insertMany(
    const std::vector<std::pair<int, int>>& entries) {

    if (entries.empty()) {
        return;
    }

    std::unordered_set<int> newKeys;
    newKeys.reserve(entries.size());

    // 统计当前哈希表中不存在的新 Key
    for (const auto& entry : entries) {
        int key = entry.first;

        if (!containsKey(key)) {
            newKeys.insert(key);
        }
    }

    // 计算批量插入后需要的元素总数
    const size_t requiredCount =
        static_cast<size_t>(elementCount) + newKeys.size();

    // 提前扩容，避免批量插入过程中频繁扩容
    while (static_cast<double>(requiredCount) / capacity > 0.75) {
        if (capacity > std::numeric_limits<int>::max() / 2) {
            throw std::length_error("Hash table capacity is too large.");
        }

        rehash(capacity * 2);
    }

    // 逐个插入，已有 Key 则更新 Value
    for (const auto& entry : entries) {
        insert(entry.first, entry.second);
    }
}

// 查找 Key
bool MyHashTable::find(int key, int& value) const {
    int index = hash(key);

    for (const auto& item : table[index]) {
        if (item.first == key) {
            value = item.second;
            return true;
        }
    }

    return false;
}

// 删除 Key
bool MyHashTable::remove(int key) {
    int index = hash(key);

    for (auto it = table[index].begin();
         it != table[index].end(); ++it) {

        if (it->first == key) {
            table[index].erase(it);
            --elementCount;
            return true;
        }
    }

    return false;
}

// 显示哈希表
void MyHashTable::display() const {
    for (int i = 0; i < capacity; ++i) {
        std::cout << "Bucket " << i << ": ";

        for (const auto& item : table[i]) {
            std::cout << "(" << item.first
                      << ", " << item.second << ") -> ";
        }

        std::cout << "nullptr" << std::endl;
    }
}
