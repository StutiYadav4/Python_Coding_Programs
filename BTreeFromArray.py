class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root
def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val, end=' ')
        print_tree_inorder(root.right)


nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)
print_tree_inorder(root)




