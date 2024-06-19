class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy_head.next



def create_linked_list(lst):
    dummy_head = ListNode(0)
    current = dummy_head
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next



def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")



l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print_linked_list(result)

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = addTwoNumbers(l1, l2)
print_linked_list(result)

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
print_linked_list(result)
