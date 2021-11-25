# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        
        traverse = answer
        carry = 0
        
        while l1 or l2:
            l1value = l1.val if l1 else 0
            l2value = l2.val if l2 else 0
            
            total = l1value + l2value + carry
            
            if total > 9:
                total = total % 10
                carry = 1
            else:
                carry = 0
                
            newNode = ListNode(total)
            traverse.next = newNode
            traverse = traverse.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        
        if carry == 1:
            lsb = ListNode(1)
            traverse.next = lsb
        
        return answer.next