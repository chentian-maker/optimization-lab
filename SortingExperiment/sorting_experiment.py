
import random
import time
import matplotlib.pyplot as plt


# 1. 冒泡排序
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 2. 插入排序
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# 3. 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 4. 二分查找：要求数组已经排好序
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 5. 检查算法是否正确
if __name__ == "__main__":
    test_data = [8, 3, 5, 1, 9, 2]
    expected = sorted(test_data)

    assert bubble_sort(test_data) == expected
    assert insertion_sort(test_data) == expected
    assert merge_sort(test_data) == expected

    sorted_data = merge_sort(test_data)
    assert sorted_data[binary_search(sorted_data, 5)] == 5
    assert binary_search(sorted_data, 100) == -1

    print("四种算法的基本测试全部通过！")

    # 6. 准备运行时间实验
    sizes = [100, 300, 600, 1000, 2000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }

    results = {name: [] for name in algorithms}

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        for name, func in algorithms.items():
            start = time.perf_counter()
            output = func(data)
            elapsed = time.perf_counter() - start

            assert output == sorted(data)
            results[name].append(elapsed)

        # 对二分查找单独计时，避免把排序时间算进去
        sorted_data = sorted(data)
        target = sorted_data[-1]

        start = time.perf_counter()
        binary_search(sorted_data, target)
        elapsed = time.perf_counter() - start

        if "Binary Search" not in results:
            results["Binary Search"] = []

        results["Binary Search"].append(elapsed)

        print(f"数组规模 {size}：测试完成")

    # 7. 绘制运行时间图
    plt.figure(figsize=(10, 6))

    for name, times in results.items():
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Array Size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Sorting and Binary Search Runtime Comparison")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # 保存真正由 Matplotlib 绘制的图
    plt.savefig("sorting_runtime.png", dpi=200)
    print("实验图已保存：sorting_runtime.png")

    plt.show()
