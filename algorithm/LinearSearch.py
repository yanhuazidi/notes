# 顺序查找（线性查找）示例


def linear_search(data, key):
    lens = len(data)
    for i in range(lens):
        if data[i] == key:
            return i
    return -1


if __name__ == '__main__':
    values = [10, 34, 56, 9, 12, 3, 76, 45, 99, 84, 25, 67]

    # 查找数据25
    result = linear_search(values, 25)
    if result == -1:
        print('未找到该数据')
    else:
        print('该数据对于的下标为：{}'.format(result))
