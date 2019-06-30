# 快速排序算法


# 简单实现
def quick(data):
    if len(data) < 2:
        return data
    mark = data[0]
    smaller = [x for x in data if x < mark]
    equal = [x for x in data if x == mark]
    bigger = [x for x in data if x > mark]
    return quick(smaller) + equal + quick(bigger)


# 自测代码
if __name__ == '__main__':
    values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
    print('原数据列表：', values)
    after = quick(values)
    print('快速排序后：', after)

