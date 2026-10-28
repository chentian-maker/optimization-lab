
#define MYHASHTABLE_TEST
#include "../MyHashTable.cpp"

#include <iostream>
#include <string>
using namespace std;

int passed = 0;
int failed = 0;

// 统一检查测试结果，并记录预期结果与实际结果
void check(const string& name,
           bool condition,
           const string& expected,
           const string& actual) {
    cout << (condition ? "[PASS] " : "[FAIL] ")
         << name << '\n';

    cout << "  预期结果：" << expected << '\n';
    cout << "  实际结果：" << actual << "\n\n";

    if (condition) {
        ++passed;
    } else {
        ++failed;
    }
}

int main() {
    cout << "===== MyHashTable 自动化测试 =====\n\n";

    // 测试1：空表
    {
        MyHashTable ht(7);
        int value = -1;

        bool found = ht.find(42, value);

        check("空表：查找不存在的 key",
              !found,
              "未找到（false）",
              found ? "找到（true）" : "未找到（false）");

        bool removed = ht.remove(42);

        check("空表：删除不存在的 key",
              !removed,
              "删除失败（false）",
              removed ? "删除成功（true）"
                      : "删除失败（false）");
    }

    // 测试2：重复 key 应当更新 value
    {
        MyHashTable ht(7);

        ht.insert(10, 100);
        ht.insert(10, 200);

        int value = -1;
        bool found = ht.find(10, value);

        check("重复 key：更新 value",
              found && value == 200,
              "找到 key=10，value=200",
              found ? "找到 key=10，value="
                          + to_string(value)
                    : "未找到 key=10");
    }

    // 测试3：负数 key
    {
        MyHashTable ht(7);

        ht.insert(-1, 77);

        int value = -1;
        bool found = ht.find(-1, value);

        check("负数 key：插入并查找 -1",
              found && value == 77,
              "找到 key=-1，value=77",
              found ? "找到 key=-1，value="
                          + to_string(value)
                    : "未找到 key=-1");
    }

    // 测试4：冲突 key
    // 1001 % 7 == 0，1008 % 7 == 0
    {
        MyHashTable ht(7);

        ht.insert(1001, 11);
        ht.insert(1008, 88);

        int value1 = -1;
        bool found1 = ht.find(1001, value1);

        check("冲突 key：查找 1001",
              found1 && value1 == 11,
              "找到 key=1001，value=11",
              found1 ? "找到 key=1001，value="
                           + to_string(value1)
                     : "未找到 key=1001");

        int value2 = -1;
        bool found2 = ht.find(1008, value2);

        check("冲突 key：查找 1008",
              found2 && value2 == 88,
              "找到 key=1008，value=88",
              found2 ? "找到 key=1008，value="
                           + to_string(value2)
                     : "未找到 key=1008");

        bool removed = ht.remove(1001);

        check("冲突 key：删除 1001",
              removed,
              "删除成功（true）",
              removed ? "删除成功（true）"
                      : "删除失败（false）");

        int value3 = -1;
        bool found3 = ht.find(1008, value3);

        check("冲突 key：删除 1001 后，1008 仍存在",
              found3 && value3 == 88,
              "找到 key=1008，value=88",
              found3 ? "找到 key=1008，value="
                           + to_string(value3)
                     : "未找到 key=1008");
    }

    // 测试5：删除不存在的 key
    {
        MyHashTable ht(7);

        ht.insert(5, 50);

        // 999 % 7 == 5，与 key=5 映射到同一个桶
        bool removed = ht.remove(999);

        check("删除不存在的 key：remove(999)",
              !removed,
              "删除失败（false）",
              removed ? "删除成功（true）"
                      : "删除失败（false）");

        int value = -1;
        bool found = ht.find(5, value);

        check("删除不存在的 key：原有数据仍存在",
              found && value == 50,
              "找到 key=5，value=50",
              found ? "找到 key=5，value="
                          + to_string(value)
                    : "未找到 key=5");
    }

    cout << "===== 测试汇总 =====\n";
    cout << "通过：" << passed << '\n';
    cout << "失败：" << failed << '\n';

    return failed == 0 ? 0 : 1;
}
