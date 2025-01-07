# 冒泡排序函数
def sort(arr):
    """
    冒泡排序函数
    :param arr: 待排序的数组
    :return: 排序后的数组
    """
    n = len(arr)
    # 遍历数组中的每一个元素
    for i in range(n):
        # 遍历数组中的每一个元素，从后往前比较
        for j in range(n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr