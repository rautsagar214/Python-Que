class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def findPairWithSumX(head, X):
    if not head:
        print(-1)
        return
    
    current = head
    found = False

    while current:
        runner = head
        while runner != current:
            if runner.data + current.data == X:
                found = True
                # Print the pair in sorted order
                print(min(current.data, runner.data), max(current.data, runner.data))
                break
            runner = runner.next
        if found:
            break
        current = current.next
    
    if not found:
        print(-1)

def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        newNode = Node(value)
        current.next = newNode
        current = newNode
    return head

# Read input
n, X = map(int, input().split())
values = list(map(int, input().split()))

# Create linked list from input values
head = createLinkedList(values)

# Find and print the pair with sum X
findPairWithSumX(head, X)
