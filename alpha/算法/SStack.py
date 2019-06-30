# 基于顺序存储的栈结构


class SStack:
    # 构建空栈
    def __init__(self):
        self._elem = []

    # 判空
    def is_empty(self):
        return self._elem == []

    #　判满　(因使用list无固定大小来实现，故不需要判满)

    #　压入数据
    def push(self, elem):
        self._elem.append(elem)
        # 测试：打印当前栈中数据
        print(self._elem)

    # 弹出数据
    def pop(self):
        # 需要判断栈是否为空
        if self.is_empty():
            raise IndexError("stack error:试图从空栈中弹出数据")
        return self._elem.pop()


# 自测代码
if __name__ == "__main__":
    # 创建自己的栈
    mystack = SStack()
    #　压入数据 10/20/30/40
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.push(40)
    # 弹出所有数据
    while not mystack.is_empty():
        print(mystack.pop())
    #　试图从空栈中弹出数据
    # mystack.pop()
