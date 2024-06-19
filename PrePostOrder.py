class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

print("Pre-order traversal:")
pre_order_traversal(root)
print("\nPost-order traversal:")
post_order_traversal(root)
