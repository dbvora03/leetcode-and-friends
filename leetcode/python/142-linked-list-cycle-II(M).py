# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        
        if head is None or head.next is None:
            return None
        
        visited = {}
        
        compare_me = head
        counter = 0
        
        while compare_me:
            
            if compare_me in visited:
                return compare_me
            else:
                visited[compare_me] = counter
            
            counter += 1
            compare_me = compare_me.next
        
        return None