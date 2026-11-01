#include <iostream>

#define MYHASHTABLE_TEST
#include "../MyHashTable.cpp"

using namespace std;


int main() {
    MyHashTable ht(7);

    cout << "第一次插入 key=10, value=100\n";
    ht.insert(10, 100);

    cout << "第二次插入 key=10, value=200\n";
    ht.insert(10, 200);

    int value = -1;
    bool found = ht.find(10, value);

    cout << "查找结果："
         << "found=" << found
         << ", value=" << value
         << ", size=" << ht.size()
         << '\n';

    return 0;
}