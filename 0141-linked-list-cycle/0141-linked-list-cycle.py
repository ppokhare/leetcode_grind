# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) space and O(n) time: put the node in the set and check if it exist
        #O(1) space and O(n) time: tortoise and hare
        
        if not head or not head.next: return False
        
        s, f = head,head.next
        
        while s and f:
            
            if s ==f: return True
            s = s.next 
            
            if f.next: 
                f = f.next.next
            else:
                break
        return False
            