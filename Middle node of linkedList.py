class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Store the data value of the node
        self.next = next  # Initialize the next pointer

# Function to find the middle of the linked list
def find_middle(head):
    if not head:  # Edge case: empty list
        return None
    
    slow = head  # Initialize the slow pointer to the head of the list
    fast = head  # Initialize the fast pointer to the head of the list

    # Move slow pointer one step and fast pointer two steps
    while fast and fast.next:
        slow = slow.next  # Slow pointer moves one step
        fast = fast.next.next  # Fast pointer moves two steps

    return slow.val  # Slow pointer will be at the middle

# Function to create a linked list from a list of elements
def create_linked_list(elements):
    if not elements:  # Edge case: empty list
        return None

    head = ListNode(elements[0])  # Create the head of the list
    current = head  # Set the current node to head
    for val in elements[1:]:
        current.next = ListNode(val)  # Create the next node
        current = current.next  # Move to the next node
    return head

# Reading input
N = int(input("Enter the number of elements in the linked list: "))  # Number of nodes in the list
if N == 0:
    print("Empty list has no middle element.")
else:
    elements = list(map(int, input("Enter the list elements: ").split()))  # Elements of the list

    # Create the linked list with the provided elements
    head = create_linked_list(elements)

    # Find and print the middle element
    middle_value = find_middle(head)
    if middle_value is not None:
        print(middle_value)
    else:
        print("The list is empty.")
