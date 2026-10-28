def binary_search(arr, target):
    """在升序数组 arr 中查找 target，返回索引；不存在返回 -1。"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 7))  # 3
    print(binary_search([1, 3, 5, 7, 9], 2))  # -1
