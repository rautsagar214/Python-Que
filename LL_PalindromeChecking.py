class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Helper function to copy a linked list
        def copyLinkedList(node):
            dummy = ListNode(0)
            current = dummy
            while node:
                current.next = ListNode(node.val)
                current = current.next
                node = node.next
            return dummy.next
        
        # Edge case: empty or single-node linked list is always a palindrome
        if not head or not head.next:
            return True
        
        # Make a copy of the original linked list and reverse it
        copied_list = copyLinkedList(head)
        reversed_copied_list = reverseLinkedList(copied_list)
        
        # Compare each corresponding node of the original and reversed lists
        while head and reversed_copied_list:
            if head.val != reversed_copied_list.val:
                return False
            head = head.next
            reversed_copied_list = reversed_copied_list.next
        
        # If all corresponding nodes have the same values, it's a palindrome
        return True

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

if __name__ == "__main__":
    n = int(input("Enter the size of the linked list: "))
    arr = list(map(int, input("Enter the elements of the linked list: ").split()))
    
    if len(arr) != n:
        print("The number of elements does not match the size specified.")
    else:
        solution = Solution()
        head = create_linked_list(arr)
        if solution.isPalindrome(head):
            print("True")
        else:
            print("False")
