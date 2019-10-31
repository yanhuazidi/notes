# 二分查找（折半查找）示例


# 递归实现
def binary_search_recur(data, key, left_index, right_index):
    if right_index < left_index:
        return -1
    middle = (left_index + right_index) // 2
    if data[middle] == key:
        return middle
    elif data[middle] > key:
        return binary_search_recur(data, key, left_index, middle-1)
    else:
        return binary_search_recur(data, key, middle+1, right_index)


# 循环实现
def binary_search_loop(data, key):
    left_index = 0
    right_index = len(data) - 1
    while left_index <= right_index:
        middle = (left_index + right_index) // 2
        if data[middle] == key:
            return middle
        elif data[middle] > key:
            right_index = middle - 1
        else:
            left_index = middle + 1
    return -1


if __name__ == '__main__':
    values = [10, 34, 56, 9, 12, 3, 76, 45, 99, 84, 25, 67]
    # 将表格按照升序排列
    values.sort()
    # 二分查找 - 递归方式
    print("二分查找 - 递归方式:")
    # 查找数据25
    result = binary_search_recur(values, 25, 0, len(values) - 1)
    if result == -1:
        print('未找到该数据')
    else:
        print('该数据对于的下标为：{}'.format(result))

    # 二分查找 - 循环方式
    print("二分查找 - 循环方式:")
    # 查找数据25
    result = binary_search_loop(values, 25)
    if result == -1:
        print('未找到该数据')
    else:
        print('该数据对于的下标为：{}'.format(result))
