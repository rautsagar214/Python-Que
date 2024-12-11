class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
        self.prev = None

def reversePrint(head):
    if not head:
        print(" ")
        return
    
    # Go to the last node
    current = head
    while current.next:
        current = current.next
    
    # Print the values from the last node to the first
    while current:
        print(current.data, end=" ")
        current = current.prev
    print()

def createDoublyLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        newNode = Node(value)
        current.next = newNode
        newNode.prev = current
        current = newNode
    return head

# Read input
n = int(input())
values = list(map(int, input().split()))

# Create doubly linked list from input values
head = createDoublyLinkedList(values)

# Print the reversed doubly linked list
reversePrint(head)
