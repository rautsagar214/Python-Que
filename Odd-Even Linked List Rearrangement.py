class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def rearrangeList(head):
    if not head or not head.next:
        return
    
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead

def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Read input
size = int(input())
values = list(map(int, input().split()))

# Create linked list from input values
head = createLinkedList(values)

# Rearrange the linked list
rearrangeList(head)

# Print the rearranged linked list
printList(head)
