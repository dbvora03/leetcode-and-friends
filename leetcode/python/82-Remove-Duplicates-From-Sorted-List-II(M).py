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
        
        current = head
        visited = {}
        while current:
            if current.val in visited:
                visited[current.val] += 1
            else:
                visited[current.val] = 1
        
            current = current.next
                
        temp_node = ListNode(0, head)
        
        prev = temp_node
        current = temp_node.next
        
        while current:
            if visited[current.val] > 1:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        
        return temp_node.next