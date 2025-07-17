# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Approach 1: Reverse LL,  Remove element, Again Reverse LL
        #Approach 2: Two pointer (Better, Optimized approach)
        dummy = ListNode(0, head)
        left = dummy
        
        right = head
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left, right = left.next, right.next
        
        #delete
        left.next = left.next.next
        return dummy.next
