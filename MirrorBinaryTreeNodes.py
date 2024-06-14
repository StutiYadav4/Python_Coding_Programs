# Mirroring the nodes of a Binary tree that is swapping the left nodes with the right and so on.

from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None

def insertNode(root,data):
    if root is None:
        root=Node(data)
        return root

    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        if temp.left is None:
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)
    return root

def inorderTraversal(root):
    if not root:
        return None
    inorderTraversal(root.left)
    print(root.data,end=" ")
    inorderTraversal(root.right)

def preorderTraversal(root):
    if not root:
        return None
    print(root.data,end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def postorderTraversal(root):
    if not root:
        return None
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data,end=" ")

def mirrorNode(root):
    if not root:
        return None
    root.right, root.left = root.left, root.right
    mirrorNode(root.left)
    mirrorNode(root.right)

if __name__=="__main__" :
    root = None
    root = insertNode(root, 10)
    root = insertNode(root, 20)
    root = insertNode(root, 30)
    root = insertNode(root, 40)
    root = insertNode(root, 50)
    root = insertNode(root, 60)

    print("Pre-Order Traversal :", end=" ")
    preorderTraversal(root)
    print("\n")
    print("Post-Order Traversal :", end=" ")
    postorderTraversal(root)
    print("\n")
    print("In-Order Traversal :", end=" ")
    inorderTraversal(root)
    print("\n")
    print("Mirroring the Nodes :", end=" ")
    mirrorNode(root)
    print("\n")
    print("Pre-Order Traversal :", end=" ")
    preorderTraversal(root)
    print("\n")



