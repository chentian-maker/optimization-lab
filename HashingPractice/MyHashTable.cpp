
#include <iostream>
#include <vector>
#include <list>
#include <utility>
#include <stdexcept>
#include <limits>
#include <unordered_set>

using namespace std;

class MyHashTable {
private:
    int capacity;
    vector<list<pair<int, int>>> table;
    int elementCount;

    static int checkedCapacity(int size) {
        if (size <= 0) {
            throw invalid_argument("Capacity must be positive.");
        }
        return size;
    }

    int hash(int key) const {
        return ((key % capacity) + capacity) % capacity;
    }

    bool containsKey(int key) const {
        int index = hash(key);

        for (const auto& item : table[index]) {
            if (item.first == key) {
                return true;
            }
        }

        return false;
    }

    void rehash(int newCapacity) {
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

public:
    MyHashTable(int size)
        : capacity(checkedCapacity(size)),
          table(capacity),
          elementCount(0) {
    }

    int size() const {
        return elementCount;
    }

    int bucketCount() const {
        return capacity;
    }

    double loadFactor() const {
        return static_cast<double>(elementCount) / capacity;
    }

    void insert(int key, int value) {
        int index = hash(key);

        for (auto& item : table[index]) {
            if (item.first == key) {
                item.second = value;
                return;
            }
        }

        if (static_cast<double>(elementCount + 1) / capacity > 0.75) {
            if (capacity > numeric_limits<int>::max() / 2) {
                throw length_error("Hash table capacity is too large.");
            }

            rehash(capacity * 2);
            index = hash(key);
        }

        table[index].push_front({key, value});
        ++elementCount;
    }

    // 批量插入：使用 unordered_set 统计需要新增的 key
    void insertMany(const vector<pair<int, int>>& entries) {
        if (entries.empty()) {
            return;
        }

        unordered_set<int> newKeys;
        newKeys.reserve(entries.size());

        for (const auto& entry : entries) {
            int key = entry.first;

            if (!containsKey(key)) {
                newKeys.insert(key);
            }
        }

        const size_t requiredCount =
            static_cast<size_t>(elementCount) + newKeys.size();

        while (static_cast<double>(requiredCount) / capacity > 0.75) {
            if (capacity > numeric_limits<int>::max() / 2) {
                throw length_error("Hash table capacity is too large.");
            }

            rehash(capacity * 2);
        }

        for (const auto& entry : entries) {
            insert(entry.first, entry.second);
        }
    }

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

#endif
