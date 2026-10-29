
#define MYHASHTABLE_TEST
#include "../MyHashTable.cpp"
#include <stdexcept>
#include <cassert>
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


    // 测试：容量为0时应抛出异常
{
    bool caught = false;

    try {
        MyHashTable ht(0);
    } catch (const invalid_argument&) {
        caught = true;
    }

    check("非法容量：0",
          caught,
          "抛出 invalid_argument",
          caught ? "捕获到异常" : "没有捕获到异常");
}

// 测试：容量为负数时应抛出异常
{
    bool caught = false;

    try {
        MyHashTable ht(-1);
    } catch (const invalid_argument&) {
        caught = true;
    }

    check("非法容量：-1",
          caught,
          "抛出 invalid_argument",
          caught ? "捕获到异常" : "没有捕获到异常");
}

// 测试：容量为1时应创建成功
{
    bool created = false;

    try {
        MyHashTable ht(1);
        created = ht.bucketCount() == 1;
    } catch (const exception&) {
        created = false;
    }

    check("合法容量：1",
          created,
          "成功创建，桶数量为1",
          created ? "创建成功" : "创建失败");
}
    // 测试0：学习 assert
    {
        int example = 100;

        assert(example == 100);

        cout << "[PASS] assert 示例\n";
        cout << "  条件 example == 100 成立\n\n";
    }

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

        // 删除第一个冲突键
        bool removed = ht.remove(1001);

        check("冲突 key：删除 1001",
              removed,
              "删除成功（true）",
              removed ? "删除成功（true）"
                      : "删除失败（false）");

        // 新增：确认被删除的 key 已不存在
        int deletedValue = -1;
        bool deletedFound = ht.find(1001, deletedValue);

        check("冲突 key：删除后 1001 不存在",
              !deletedFound,
              "find(1001) 返回 false",
              deletedFound ? "仍然找到 key=1001"
                           : "未找到 key=1001");

        // 确认删除一个冲突键没有影响另一个键
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

    // 测试6：批量插入、查找和自动扩容
    {
        MyHashTable ht(7);

        // 插入100个键值对
        for (int i = 0; i < 100; ++i) {
            ht.insert(i, i * 10);
        }

        // 验证100个 key，并定位第一个错误
        bool allCorrect = true;
        int value = -1;
        string errorMessage = "100个 key 全部正确";

        for (int i = 0; i < 100; ++i) {
            bool found = ht.find(i, value);

            if (!found) {
                allCorrect = false;
                errorMessage =
                    "查找失败，key=" + to_string(i);
                break;
            }

            if (value != i * 10) {
                allCorrect = false;
                errorMessage =
                    "value 错误，key=" + to_string(i)
                    + "，预期=" + to_string(i * 10)
                    + "，实际=" + to_string(value);
                break;
            }
        }

        check("批量测试：插入并查找100个 key",
              allCorrect,
              "100个 key 全部找到，value 均正确",
              errorMessage);

        // 检查自动扩容
        check("自动扩容：桶数量增加",
              ht.bucketCount() > 7,
              "桶数量大于7",
              "桶数量=" + to_string(ht.bucketCount()));

        // 检查元素数量
        check("元素数量：100个 key",
              ht.size() == 100,
              "size=100",
              "size=" + to_string(ht.size()));

        // 检查负载因子
        check("负载因子：不超过0.75",
              ht.loadFactor() <= 0.75,
              "loadFactor <= 0.75",
              "loadFactor=" + to_string(ht.loadFactor()));
    }

    // 测试7：重复插入、扩容和删除的综合测试
    {
        MyHashTable ht(7);

        // 测试7.1：重复插入同一个 key
        ht.insert(1, 10);
        ht.insert(1, 20);

        int value = -1;
        bool found = ht.find(1, value);

        check("重复插入：更新 value 且不增加 size",
              found && value == 20 && ht.size() == 1,
              "value=20, size=1",
              "value=" + to_string(value)
                  + ", size=" + to_string(ht.size()));

        // 测试7.2：继续插入大量数据，触发自动扩容
        for (int i = 2; i <= 30; ++i) {
            ht.insert(i, i * 10);
        }

        check("综合测试：扩容后数据数量正确",
              ht.size() == 30 && ht.bucketCount() > 7,
              "size=30 且桶数量大于7",
              "size=" + to_string(ht.size())
                  + ", 桶数量="
                  + to_string(ht.bucketCount()));

        // 测试7.3：删除存在的 key，size 应减一
        bool removed = ht.remove(10);

        check("删除存在的 key：size 减一",
              removed && ht.size() == 29,
              "删除成功，size=29",
              string(removed ? "删除成功" : "删除失败")
                  + ", size=" + to_string(ht.size()));

        // 测试7.4：删除不存在的 key，size 不应改变
        removed = ht.remove(9999);

        check("删除不存在的 key：size 不变",
              !removed && ht.size() == 29,
              "删除失败，size=29",
              string(removed ? "删除成功" : "删除失败")
                  + ", size=" + to_string(ht.size()));

        // 测试7.5：扩容后，原有数据仍然正确
        value = -1;
        found = ht.find(1, value);

        check("扩容后：原有 key-value 保持正确",
              found && value == 20,
              "找到 key=1，value=20",
              found ? "找到 key=1，value=" + to_string(value)
                    : "未找到 key=1");
    }

    // 输出测试汇总
    cout << "===== 测试汇总 =====\n";
    cout << "通过：" << passed << '\n';
    cout << "失败：" << failed << '\n';
    cout << "总计：" << passed + failed << '\n';

    return failed == 0 ? 0 : 1;
}
