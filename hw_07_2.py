class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min_value(node):
    current = node
    # Ітеруємося по лівих нащадках, поки не дійдемо до кінцевого вузла
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Найменше значення у дереві:", find_min_value(root))