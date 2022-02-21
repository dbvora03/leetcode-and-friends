# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        prev_point = None
        curr_point = head
        
        while curr_point:
            
            next_point = curr_point.next
            curr_point.next = prev_point
            
            prev_point = curr_point
            curr_point = next_point
        
        return prev_point
            