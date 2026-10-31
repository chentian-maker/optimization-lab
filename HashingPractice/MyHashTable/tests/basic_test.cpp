#include <iostream>
#include "MyHashTable.h"
#include <stdexcept>

using namespace std;

int main() {

    // 测试1：容量为0
    cout << "===== Test 1 =====" << endl;

    try {
        MyHashTable ht(0);
        cout << "Test Failed" << endl;
    }
    catch (const invalid_argument& e) {
        cout << "Test Passed: " << e.what() << endl;
    }

    // 测试2：插入负数Key
    cout << "\n===== Test 2 =====" << endl;

    MyHashTable ht(7);

    ht.insert(-8, 100);

    int value = -1;
    bool found = ht.find(-8, value);

    if (found && value == 100) {
        cout << "Test Passed" << endl;
    } else {
        cout << "Test Failed" << endl;
    }

    // 测试3：删除不存在的Key
    cout << "\n===== Test 3 =====" << endl;

    bool removed = ht.remove(9999);

    if (!removed && ht.size() == 1) {
        cout << "Test Passed" << endl;
    } else {
        cout << "Test Failed" << endl;
    }

    return 0;
}