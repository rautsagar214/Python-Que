# Definition for singly-linked list.
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Set the next node to None

def sortList(head):
    # Initialize counts of 0, 1, and 2 as 0
    count = [0, 0, 0]

    # Traverse the linked list and count 0s, 1s, and 2s
    current = head
    while current:
        count[current.data] += 1
        current = current.next

    # Update the linked list with sorted order based on the counts
    current = head
    index = 0
    while current:
        # Skip if count of current index (0, 1, 2) is zero
        if count[index] == 0:
            index += 1
        else:
            # Assign the value to the current node
            current.data = index
            # Decrease the count for the assigned value
            count[index] -= 1
            # Move to the next node
            current = current.next

    return head

# Helper function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Helper function to create a linked list from a list of values
def createList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Taking input in the format provided
size_of_list = int(input("Enter the size of the list: "))
input_values = input("Enter the values of the linked list (only 0s, 1s, and 2s) separated by space: ")
arr = list(map(int, input_values.split()))

# Ensure the list size matches the provided size
if len(arr) != size_of_list:
    print("The number of values entered does not match the specified size of the list.")
else:
    # Create linked list from user input
    head = createList(arr)

    # Sort the list
    sorted_head = sortList(head)

    # Output the sorted list
    print("Sorted linked list:")
    printList(sorted_head)
