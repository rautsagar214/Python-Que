# finding nth element from end



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        
        curr.next = newNode
        
        
        
    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data , end=" ")
            curr = curr.next
    
    def remove_at_k(self,k):
        dummy = Node(0)
        dummy.next = self.head
        self.head = dummy
        
        first = dummy
        second = dummy
        
        for i in range(k+1):
            if first is None:
                return self.head.next
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next

    # Remove the nth node from end
        if second.next:
            second.next = second.next.next
        else:
            second.next = None
    
        self.head = self.head.next   
        
        
n = int(input())

arr= list(map(int,input().split()))

k = int(input())

ll = Linkedlist()

for i in arr:
    ll.append(i)
    
ll.remove_at_k(k)
ll.printList()
    

