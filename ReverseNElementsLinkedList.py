class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_first_n(head, n):
    if n <= 0 or not head:
        return head

    prev = None
    current = head
    next_node = None
    count = 0
    temp = head
    while temp and count < n:
        temp = temp.next
        count += 1
    if count < n:
        return head
    count = 0
    while current and count < n:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    head.next = current

    return prev
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original list:")
print_list(head)
head = reverse_first_n(head, 3)
print("List after reversing first 3 elements:")
print_list(head)

