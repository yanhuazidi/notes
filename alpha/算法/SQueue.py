# 基于顺序存储的队列结构
class SQueue:
    # 创建空队列
    def __init__(self):
        self._elem = []
    # 判空
    def is_empty(self):
        return self._elem == []
    #　判满　(因使用list无固定大小来实现，故不需要判满)
    # 压入数据
    def push(self, data):
        # 从列表头插入数据
        self._elem.insert(0, data)
    # 弹出数据
    def pop(self):
        # 需要判断队列是否为空
        if self.is_empty():
            raise IndexError("stack error:试图从空栈中弹出数据")
        # 从列表尾移出数据
        return self._elem.pop()


#　自测代码
if __name__ == "__main__":
    # 创建自己的队列
    myqueue = SQueue()
    # 压入数据 aaa/bbb/ccc/ddd
    myqueue.push('aaa')
    myqueue.push('bbb')
    myqueue.push('ccc')
    myqueue.push('ddd')
    # 弹出数据
    while not myqueue.is_empty():
        print(myqueue.pop())
    # 空队列中获取数据
    # myqueue.pop()
