# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        prev = head
        current = head.next
        
        visited = set()
        
        visited.add(prev.val)
        
        while current:
            if current.val in visited:
                prev.next = current.next
                current = current.next
            else:
                visited.add(current.val)
                current = current.next
                prev = prev.next
        
        return head