class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, new_data):
        new_node = Node(new_data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Set the new node as the next of the last node

    def remove_all_occurrences(self, key):
        temp = self.head  # Start from the head
        prev = None
        while temp:  # Traverse the list
            if temp.data == key:  # If the current node's data is equal to the key
                if prev:  # If it's not the head node
                    prev.next = temp.next  # Remove the current node
                else:  # If it's the head node
                    self.head = temp.next  # Update the head
            else:
                prev = temp  # Update the previous node
            temp = temp.next  # Move to the next node

    def print_list(self):
        temp = self.head  # Start from the head
        while temp:  # Traverse the list
            print(temp.data, end=" ")  # Print the data of each node
            temp = temp.next  # Move to the next node
        print()  # Print a newline at the end

# Taking input from the user
N = int(input("Enter the number of nodes: "))  # Number of nodes
X = int(input("Enter the value to be deleted: "))  # Value to be deleted
elements = list(map(int, input("Enter the elements separated by space: ").split()))  # List of elements

# Creating and modifying the linked list
ll = LinkedList()  # Create a new linked list
for elem in elements:  # Append each element to the list
    ll.append(elem)

ll.remove_all_occurrences(X)  # Remove all occurrences of the specified value
ll.print_list()  # Output the modified linked list
