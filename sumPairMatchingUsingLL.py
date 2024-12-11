class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def find_pair_with_sum(head, X):
    current = head
    elements = set()
    while current:
        complement = X - current.data
        if complement in elements:
            first, second = sorted([current.data, complement])
            print(first, second)
            return
        elements.add(current.data)
        current = current.next
    print(-1)

if __name__ == "__main__":
    ll = LinkedList()
    
    n = int(input())
    X = int(input())
    values = list(map(int, input().split()))
    
    for val in values:
        ll.append(val)
        
    find_pair_with_sum(ll.head, X)
