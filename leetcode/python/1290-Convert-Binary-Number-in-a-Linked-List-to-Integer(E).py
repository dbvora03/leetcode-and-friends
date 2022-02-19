# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        total = 0
        traverse = head
        
        while traverse:
            total += traverse.val
            total *= 2
            traverse = traverse.next
        
        return total // 2