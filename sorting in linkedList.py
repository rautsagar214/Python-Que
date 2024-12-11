class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        node = self.head
        result = []
        while node:
            result.append(node.data)
            node = node.next
        return result

    def from_list(self, lst):
        self.head = None
        for data in lst:
            self.append(data)

    def sort(self):
        lst = self.to_list()
        lst.sort()
        self.from_list(lst)

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

# Taking input from the user
N = int(input("Enter the number of nodes: "))
elements = list(map(int, input("Enter the elements separated by space: ").split()))

# Creating and sorting the linked list
ll = LinkedList()
for elem in elements:
    ll.append(elem)

ll.sort()
ll.print_list()  # Output the sorted linked list
