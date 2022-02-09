# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        lists = []
        first_k = []
        traverse = head
        while traverse:
            first_k.append(traverse.val)
            if len(first_k) == k:
                lists.append(first_k)
                first_k = []
            
            traverse = traverse.next

        new_head = ListNode(0)
        traverse = new_head
        
        for sets in lists:
            while len(sets) > 0:
                value = sets.pop()
                traverse.next = ListNode(value)
                traverse = traverse.next
        
        while len(first_k) > 0:
            value = first_k.pop(0)
            traverse.next = ListNode(value)
            traverse = traverse.next
        
        head = new_head.next
        
        return head