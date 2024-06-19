class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        left_height, left_balanced = check_height(node.left)
        right_height, right_balanced = check_height(node.right)
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height <= 1)
        current_height = max(left_height, right_height) + 1

        return current_height, current_balanced
    balanced = check_height(root)
    return balanced

balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)

unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.left.left = TreeNode(3)

print(is_balanced(balanced_root))
print(is_balanced(unbalanced_root))
