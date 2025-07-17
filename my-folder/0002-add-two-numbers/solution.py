# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        carry = 0
        while l1 or l2 or carry:
            currVal = carry
            if l1:
                currVal += l1.val
                l1 = l1.next
            if l2:
                currVal += l2.val
                l2 = l2.next
            value = currVal % 10
            carry = currVal // 10

            dummy.next = ListNode(value)
            dummy = dummy.next
        return res.next
            
            
