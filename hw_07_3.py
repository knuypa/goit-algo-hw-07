class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Сума всіх значень у дереві:", sum_of_values(root)) 