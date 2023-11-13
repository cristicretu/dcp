from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value} has childs {self.left} and {self.right}"


def print_level_order(root):
    if root is None:
        return

    q = deque([root])
    level_order = []

    while q:
        # number of nodes at the current level
        nr_nodes = len(q)

        for _ in range(nr_nodes):
            element = q.popleft()

            if element.left is not None:
                q.append(element.left)
            if element.right is not None:
                q.append(element.right)

            level_order.append(element.value)

    for el in level_order:
        print(el, end=" ")


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(12)
root.right.right = TreeNode(16)

print_level_order(root)
