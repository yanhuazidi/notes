# 插入排序算法


# 简单实现
def insertion(data):
    for n in range(1, len(data)):
        tmp = data[n]
        for i in range(n, -1, -1):
            if data[i-1] < tmp or i == 0:
                break
            else:
                data[i] = data[i - 1]
        data[i] = tmp


# 自测代码
if __name__ == '__main__':
    values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
    print('原数据列表：', values)
    insertion(values)
    print('插入排序后：', values)

