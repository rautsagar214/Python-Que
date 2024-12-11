class Node:
    def __init__(self , data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self , data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node


    def insert_at_index(self , index , data):
        new_node = Node(data)

        curr = self.head
        currIndex = 0
        while currIndex != index-1:
            curr = curr.next
            currIndex += 1

        temp = curr.next
        curr.next = new_node
        new_node.next = temp

            

    def delete_at_index(self , index):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            curr = self.head
            currIndex = 0
            while currIndex != index-1:
                curr = curr.next
                currIndex += 1
            
            temp = curr.next.next
            del curr.next
            curr.next = temp
    
    def display(self):
        curr = self.head

        while curr != None:
            print(str(curr.data) + "-->" , end="")
            curr = curr.next

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    ll.insert_at_end(5)

    ll.insert_at_index(2 , 3)
    ll.delete_at_index(4)

    ll.display()


