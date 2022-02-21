# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:
            first_val = lists.pop(0)
            second_val = lists.pop(0)
            
            new_val = self.mergeTwoLists(first_val, second_val)
            lists.append(new_val)
        
        return lists[0] if lists != [] else None
    
    def mergeTwoLists(self, lista, listb):
        
        if not lista:
            return listb
        if not listb:
            return lista
        
        if lista.val > listb.val:
            listb.next = self.mergeTwoLists(lista, listb.next)
            return listb
        else:
            lista.next = self.mergeTwoLists(lista.next, listb)
            return lista
        