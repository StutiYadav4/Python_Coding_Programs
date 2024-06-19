from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None
def insert(root, data):
    if not root:
        root = Node(data)
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

def searchNode(root,target):
    if not root:
        return None
    if root.data == target:
        return root.data
    leftSearch = searchNode(root.left, target)
    if leftSearch:
        return leftSearch
    searchNode(root.right, target)


if __name__ == "__main__":
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 60)
    target = int(input("Enter the value of the node to be found :"))
    output = searchNode(root, target)
    print(output)





