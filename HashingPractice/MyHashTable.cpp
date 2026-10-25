
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

public:
    // 按照成员声明顺序初始化
    MyHashTable(int size)
        : capacity(checkedCapacity(size)), table(capacity) {
    }

    // 下面保留你原来的 insert、find、remove、display
};
    void insert(int key, int value) {
        int index = hash(key);

        // 先检查当前链表中是否已有该 Key
        for (auto& item : table[index]) {
            if (item.first == key) {
                item.second = value;
                return;
            }
        }

        // Key 不存在，添加到链表头部
        table[index].push_front({key, value});
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

int main() {
    MyHashTable ht(7);

    cout << "=== Insert ===" << endl;
    ht.insert(1001, 90);
    ht.insert(1008, 88);
    ht.insert(1002, 85);
    ht.insert(1003, 95);
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
