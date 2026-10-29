

#include <iostream>
#include <vector>
#include <list>
#include <utility>
#include <stdexcept>

using namespace std;

class MyHashTable {
private:
    // 先声明容量，再声明哈希表
    int capacity;
    vector<list<pair<int, int>>> table;
    int elementCount;

    // 检查容量是否合法
    static int checkedCapacity(int size) {
        if (size <= 0) {
            throw invalid_argument("Capacity must be positive.");
        }
        return size;
    }

    // 将 Key 映射到合法的数组索引
    int hash(int key) const {
        return ((key % capacity) + capacity) % capacity;
    }

    // 扩大桶的数量，并重新分配所有元素
    void rehash(int newCapacity) {
        // 暂存扩容前的数据
        auto oldTable = std::move(table);

        // 创建新的桶
        capacity = newCapacity;
        table.clear();
        table.resize(capacity);

        // 将原有元素重新放入新桶
        elementCount = 0;

        for (const auto& bucket : oldTable) {
            for (const auto& item : bucket) {
                int index = hash(item.first);
                table[index].push_front(item);
                ++elementCount;
            }
        }
    }

public:
    // 按照成员声明顺序初始化
    MyHashTable(int size)
        : capacity(checkedCapacity(size)),
          table(capacity),
          elementCount(0) {
    }

    // 返回当前元素数量
    int size() const {
        return elementCount;
    }

    // 返回当前桶的数量
    int bucketCount() const {
        return capacity;
    }

    // 返回当前负载因子
    double loadFactor() const {
        return static_cast<double>(elementCount) / capacity;
    }

    // 插入单个键值对；若 key 已存在，则更新 value
    void insert(int key, int value) {
        int index = hash(key);

        // 如果 key 已经存在，只更新 value
        for (auto& item : table[index]) {
            if (item.first == key) {
                item.second = value;
                return;
            }
        }

        // 如果插入新元素会使负载因子超过 0.75，则扩容
        if (static_cast<double>(elementCount + 1) / capacity > 0.75) {
            rehash(capacity * 2);

            // 容量改变后，必须重新计算桶索引
            index = hash(key);
        }

        // 将新键值对插入对应桶
        table[index].push_front({key, value});
        ++elementCount;
    }

    // 批量插入键值对
    // 复用 insert()，统一处理重复 key、负数 key 和自动扩容
    void insertMany(const vector<pair<int, int>>& entries) {
        for (const auto& entry : entries) {
            insert(entry.first, entry.second);
        }
    }

    // 查找 Key：成功返回 true，并通过引用返回 Value
    bool find(int key, int& value) const {
        int index = hash(key);

        for (const auto& item : table[index]) {
            if (item.first == key) {
                value = item.second;
                return true;
            }
        }

        return false;
    }

    // 删除指定 Key；找到并删除时返回 true
    bool remove(int key) {
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

    // 打印所有桶及其链表
    void display() const {
        for (int i = 0; i < capacity; ++i) {
            cout << "Bucket " << i << ": ";

            for (const auto& item : table[i]) {
                cout << "(" << item.first
                     << ", " << item.second << ") -> ";
            }

            cout << "nullptr" << endl;
        }
    }
};

#ifndef MYHASHTABLE_TEST
int main() {
    MyHashTable ht(7);

    cout << "=== Insert ===" << endl;
    ht.insert(1001, 90);
    ht.insert(1008, 88);
    ht.insert(1002, 85);
    ht.insert(1003, 95);
    ht.display();

    cout << "\n=== Batch Insert ===" << endl;
    ht.insertMany({
        {10, 100},
        {20, 200},
        {30, 300},
        {10, 999}
    });
    ht.display();

    cout << "\n=== Find ===" << endl;
    int value = 0;

    if (ht.find(1008, value)) {
        cout << "Key 1008 found, value = "
             << value << endl;
    } else {
        cout << "Key 1008 not found" << endl;
    }

    cout << "\n=== Update ===" << endl;
    ht.insert(1008, 92);
    ht.find(1008, value);
    cout << "Updated value of 1008 = "
         << value << endl;

    cout << "\n=== Remove ===" << endl;
    if (ht.remove(1001)) {
        cout << "Key 1001 removed" << endl;
    }

    ht.display();

    cout << "\n=== Find Missing Key ===" << endl;
    if (!ht.find(9999, value)) {
        cout << "Key 9999 not found" << endl;
    }

    return 0;
}
#endif
