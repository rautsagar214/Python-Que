class Node:
    def __init__(self, data=None):
        self.data = data  # Initialize the node with data
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Set the new node as the next of the last node
        new_node.prev = last  # Set the previous of the new node to the last node

    def insert_at_position(self, k, val):
        new_node = Node(val)  # Create a new node with the given value
        if k == 0:  # If the position is 0
            new_node.next = self.head  # Set the new node's next to the current head
            if self.head:  # If the list is not empty
                self.head.prev = new_node  # Set the current head's previous to the new node
            self.head = new_node  # Set the new node as the head
            return
        temp = self.head  # Start from the head
        for _ in range(k - 1):  # Traverse to the node before the position
            if temp is None:  # If the position is out of bounds
                return
            temp = temp.next
        if temp is None:  # If the position is out of bounds
            return
        new_node.next = temp.next  # Set the new node's next to the current node's next
        new_node.prev = temp  # Set the new node's previous to the current node
        if temp.next:  # If the current node's next is not None
            temp.next.prev = new_node  # Set the next node's previous to the new node
        temp.next = new_node  # Set the current node's next to the new node

    def print_list(self):
        temp = self.head  # Start from the head
        while temp:  # Traverse the list
            print(temp.data, end=" ")  # Print the data of each node
            temp = temp.next  # Move to the next node
        print()  # Print a newline at the end

# Taking input from the user
N = int(input("Enter the number of nodes: "))  # Number of nodes
K = int(input("Enter the position to insert the new node: "))  # Position to insert the new node
val = int(input("Enter the value of the new node: "))  # Value of the new node
elements = list(map(int, input("Enter the elements separated by space: ").split()))  # List of elements

# Creating and modifying the doubly linked list
dll = DoublyLinkedList()  # Create a new doubly linked list
for elem in elements:  # Append each element to the list
    dll.append(elem)

dll.insert_at_position(K, val)  # Insert the new node at the specified position
dll.print_list()  # Output the modified doubly linked list
