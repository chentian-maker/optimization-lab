
def insertion_sort(numbers):
    arr = numbers.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

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

test_cases = [
    [5, 3, 4, 1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [],
    [7],
    [3, 3, 1, 2],
]

for test in test_cases:
    print("原始数据：", test)
    print("插入排序：", insertion_sort(test))
    print("归并排序：", merge_sort(test))
    print()
