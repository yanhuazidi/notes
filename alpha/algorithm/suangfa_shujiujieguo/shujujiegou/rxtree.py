

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.elem = data
        self.l_child = left
        self.r_child = right

# 二叉树类
class Tree:
    # 创建空树
    def __init__(self):
        self.root = TreeNode()
        self.incomplete = []

    # 判空
    def is_empty(self):
        return self.root.elem is None

    # 添加结点
    def add(self, data):
        # 为新数据创建结点
        tmp = TreeNode(data)
        # 若为空树：直接到对根结点赋值新结点
        # 若为非空树：添加新节点到子树不完整的结点(incomplete)
        if self.is_empty():
            self.root = tmp
            self.incomplete.append(self.root)
        else:
            first_incomplete = self.incomplete[0]
            if first_incomplete.l_child is None:
                # 左子节点为空：添加到左子节点处
                first_incomplete.l_child = tmp
                self.incomplete.append(first_incomplete.l_child)
            else:
                # 右子节点为空：添加到右子节点处
                first_incomplete.r_child = tmp
                self.incomplete.append(first_incomplete.r_child)
                self.incomplete.pop(0)

    # 先序遍历二叉树并显示
    def front_show(self, tree):
        if tree is None:
            # 遍历到最后一层结点
            return
        print(tree.elem)
        self.front_show(tree.l_child)
        self.front_show(tree.r_child)

    # 中序遍历二叉树并显示
    def middle_show(self, tree):
        if tree is None:
            # 空树
            return
        self.middle_show(tree.l_child)
        print(tree.elem)
        self.middle_show(tree.r_child)

    # 后序遍历二叉树并显示
    def post_show(self, tree):
        if tree is None:
            # 空树
            return
        self.post_show(tree.l_child)
        self.post_show(tree.r_child)
        print(tree.elem)

    # 广度优先遍历并显示
    def level_show(self):
        if self.root is None:
            # 空树
            return
        nodes = []
        current = self.root
        nodes.append(current)
        while nodes:
            current = nodes.pop(0)
            print(current.elem)
            if current.l_child is not None:
                nodes.append(current.l_child)
            if current.r_child is not None:
                nodes.append(current.r_child)

if __name__ == "__main__":
    # 产生10个数据放入二叉树中
    values = range(10)
    my_tree = Tree()
    for value in values:
        my_tree.add(value)
    # 遍历二叉树
    print("前序遍历")
    my_tree.front_show(my_tree.root)
    print("中序遍历")
    my_tree.middle_show(my_tree.root)
    print("后序遍历")
    my_tree.post_show(my_tree.root)
    print("广度优先遍历")
    my_tree.level_show()