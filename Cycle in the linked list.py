# Define a class for the linked list nodes
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value of the node
        self.next = None  # Initialize the next pointer as None

# Function to detect a cycle in the linked list
def has_cycle(head):
    slow = head  # Initialize the slow pointer to the head of the list
    fast = head  # Initialize the fast pointer to the head of the list

    while fast and fast.next:
        slow = slow.next  # Move slow pointer one step
        fast = fast.next.next  # Move fast pointer two steps

        if slow == fast:  # If the slow and fast pointers meet, a cycle is detected
            return True

    return False  # If fast pointer reaches the end, no cycle is present

# Function to create a linked list with a potential cycle based on input
def create_linked_list_with_cycle(N, elements, pos):
    head = Node(elements[0])  # Create the head of the list
    current = head  # Set the current node to head
    cycle_node = None

    if pos == 1:
        cycle_node = head  # If cycle position is 1, cycle starts at head

    for i in range(1, N):
        current.next = Node(elements[i])  # Create the next node
        current = current.next  # Move to the next node
        if i == pos - 1:
            cycle_node = current  # Mark the node where the cycle should start

    if cycle_node and pos <= N:
        current.next = cycle_node  # Create the cycle by linking the last node to the cycle node

    return head

# Reading input
N = int(input("Enter the number of nodes (N): "))  # Number of nodes in the list
elements = list(map(int, input("Enter the list elements: ").split()))  # Elements of the list
pos = int(input("Enter the position (1-based) where the tail is connected: "))  # Position to form a cycle

# Create the linked list with the specified cycle
head = create_linked_list_with_cycle(N, elements, pos)

# Check if the linked list has a cycle
result = has_cycle(head)
print(result)  # Output will be True if there's a cycle, False otherwise
