
#define MYHASHTABLE_TEST
#include "../MyHashTable.cpp"

#include <chrono>
#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>

using namespace std;
using namespace chrono;

int main() {
    const int N = 100000;
    const int REPEATS = 5;

    // 提前准备相同的数据，避免把数据生成时间算入测试
    vector<pair<int, int>> entries;
    entries.reserve(N);

    for (int i = 0; i < N; ++i) {
        entries.push_back({i, i * 10});
    }

    double singleTotal = 0.0;
    double batchTotal = 0.0;

    for (int r = 0; r < REPEATS; ++r) {
        // 测试一：逐项调用 insert()
        auto start1 = steady_clock::now();

        MyHashTable singleTable(7);

        for (const auto& entry : entries) {
            singleTable.insert(entry.first, entry.second);
        }

        auto end1 = steady_clock::now();

        double singleMs =
            duration<double, milli>(end1 - start1).count();

        singleTotal += singleMs;

        // 测试二：一次调用 insertMany()
        auto start2 = steady_clock::now();

        MyHashTable batchTable(7);
        batchTable.insertMany(entries);

        auto end2 = steady_clock::now();

        double batchMs =
            duration<double, milli>(end2 - start2).count();

        batchTotal += batchMs;

        // 检查两种方式的结果是否一致
        bool correct =
            singleTable.size() == N &&
            batchTable.size() == N &&
            singleTable.bucketCount() == batchTable.bucketCount();

        int value1 = -1;
        int value2 = -1;

        correct = correct
            && singleTable.find(N - 1, value1)
            && batchTable.find(N - 1, value2)
            && value1 == value2
            && value1 == (N - 1) * 10;

        cout << "第 " << r + 1 << " 轮：\n";
        cout << "  逐项插入：" << fixed << setprecision(3)
             << singleMs << " ms\n";
        cout << "  批量插入：" << batchMs << " ms\n";
        cout << "  数据一致性：" << (correct ? "通过" : "失败")
             << "\n\n";

        if (!correct) {
            cerr << "错误：两种插入方式的结果不一致！\n";
            return 1;
        }
    }

    double singleAvg = singleTotal / REPEATS;
    double batchAvg = batchTotal / REPEATS;

    cout << "===== 性能测试汇总 =====\n";
    cout << "数据量：" << N << '\n';
    cout << "重复次数：" << REPEATS << '\n';

    cout << fixed << setprecision(3);
    cout << "逐项插入平均耗时：" << singleAvg << " ms\n";
    cout << "批量插入平均耗时：" << batchAvg << " ms\n";

    if (batchAvg < singleAvg) {
        double improvement =
            (singleAvg - batchAvg) / singleAvg * 100.0;

        cout << "本次测试中，批量接口快约 "
             << improvement << "%\n";
    } else if (batchAvg > singleAvg) {
        double difference =
            (batchAvg - singleAvg) / singleAvg * 100.0;

        cout << "本次测试中，批量接口慢约 "
             << difference << "%\n";
    } else {
        cout << "两种方式的平均耗时相同。\n";
    }

    cout << "\n注意：小幅性能差异可能来自系统调度和计时波动。\n";
     
    
    // 场景1：小批次插入
    {
        MyHashTable ht(7);
        vector<pair<int, int>> entries = {
            {1, 10}, {2, 20}, {3, 30}, {4, 40}
        };

        auto start = steady_clock::now();
        ht.insertMany(entries);
        auto end = steady_clock::now();

        cout << "小批次插入耗时："
             << duration<double, micro>(end - start).count()
             << " 微秒，size=" << ht.size() << '\n';
    }

    // 场景2：大量重复 key，检查是否过度扩容
    {
        MyHashTable ht(7);
        ht.insert(1, 10);

        vector<pair<int, int>> entries;
        for (int i = 0; i < 10000; ++i) {
            entries.push_back({1, i});
        }

        auto start = steady_clock::now();
        ht.insertMany(entries);
        auto end = steady_clock::now();

        int value = -1;
        bool correct = ht.find(1, value) && value == 9999;

        cout << "重复 key 批次耗时："
             << duration<double, milli>(end - start).count()
             << " ms\n";
        cout << "  数据正确性：" << (correct ? "通过" : "失败") << '\n';
        cout << "  元素数量：" << ht.size() << '\n';
        cout << "  桶数量：" << ht.bucketCount() << '\n';
    }

    // 场景3：在已有数据的表中继续批量插入
    {
        MyHashTable ht(7);

        for (int i = 0; i < 1000; ++i) {
            ht.insert(i, i);
        }

        vector<pair<int, int>> entries;
        for (int i = 1000; i < 2000; ++i) {
            entries.push_back({i, i});
        }

        auto start = steady_clock::now();
        ht.insertMany(entries);
        auto end = steady_clock::now();

        cout << "已有数据后批量插入耗时："
             << duration<double, milli>(end - start).count()
             << " ms\n";
        cout << "  最终元素数量：" << ht.size() << '\n';
        cout << "  最终桶数量：" << ht.bucketCount() << '\n';
    }

    return 0;
}
