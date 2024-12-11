
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def remove_duplicates(self):
        if not self.head:
            print(" ")
            return
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
                
    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
            
    def insert_at(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    ll = LinkedList()
    for i in arr:
        ll.insert_at(i)
    ll.remove_duplicates()
    ll.display()
            
            
            
        