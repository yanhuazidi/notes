# 基于链式存储的栈结构


# 自定义节点结构
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# 链式栈
class LStack:
    # 构建空栈　－　空节点
    def __init__(self):
        self._head = Node()
        self._count = 0

    # 判空
    def is_empty(self):
        return self._count == 0

    #　判满　(因使用链式结构来实现无固定大小，故不需要判满)

    #　压入数据
    def push(self, elem):
        # 创建数据节点
        tmp = Node(elem)
        # 新节点放人栈中
        if self.is_empty():
			# 空栈时
			# 栈顶指向新数据节点
            self._head = tmp
        else:
			# 非空栈时
			# 新数据节点下一链接域指向原栈顶
            tmp.next = self._head
			# 变更栈顶位置
            self._head = tmp
        #　栈中数据节点计数加一
        self._count += 1

    # 弹出数据
    def pop(self):
        # 需要判断栈是否为空
        if self.is_empty():
            raise IndexError("stack error:试图从空栈中弹出数据")
        else:
            # 节点数目减一
            self._count -= 1
            # 保存数据
            elem = self._head.data
            # 栈顶变更
            self._head = self._head.next
            # 返回数据
            return elem


# 自测代码
if __name__ == "__main__":
    # 创建自己的栈
    mystack = LStack()
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
