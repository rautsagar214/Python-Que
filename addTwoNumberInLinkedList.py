class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a linked list from a list of numbers
def createLinkedList(numbers):
    dummy = Node(0)
    current = dummy
    for number in numbers:
        current.next = Node(number)
        current = current.next
    return dummy.next

# Function to reverse a linked list
def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to add two numbers represented by linked lists
def addTwoNumbers(l1, l2):
    # Reverse both linked lists to simplify the addition
    l1 = reverseLinkedList(l1)
    l2 = reverseLinkedList(l2)

    carry = 0  # Initialize carry to 0
    dummy = Node(0)  # Dummy node for the result linked list
    res_ll = dummy  # Pointer to traverse the result list

    # Traverse both linked lists
    while l1 or l2 or carry:
        # Get the value from the first list, if present
        val1 = l1.data if l1 else 0
        # Get the value from the second list, if present
        val2 = l2.data if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        # Create a new node with the sum and attach it to the result
        res_ll.next = Node(new_val)
        res_ll = res_ll.next  # Move to the next node in the result list

        # Move to the next nodes in both lists, if available
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    # Reverse the result to get the correct order
    return reverseLinkedList(dummy.next)

# Function to print the linked list
def printLinkedList(head):
    if not head:
        print("Empty List")
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Input
N = int(input("Enter the number of digits in the first number (N): "))
N_values = list(map(int, input(f"Enter the {N} digits (space-separated): ").split()))

M = int(input("Enter the number of digits in the second number (M): "))
M_values = list(map(int, input(f"Enter the {M} digits (space-separated): ").split()))

# Create linked lists
l1 = createLinkedList(N_values)
l2 = createLinkedList(M_values)

# Add the two numbers
result = addTwoNumbers(l1, l2)

# Print the result
print("The result of the addition is:")
printLinkedList(result)
