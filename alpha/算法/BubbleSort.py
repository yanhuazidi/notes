# 冒泡排序算法


# 简单实现
def bubble(data):
    for n in range(len(data)-1):
        for i in range(len(data)-1-n):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]


# 自测代码
if __name__ == '__main__':
    values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
    print('原数据列表：', values)
    bubble(values)
    print('冒泡排序后：', values)

