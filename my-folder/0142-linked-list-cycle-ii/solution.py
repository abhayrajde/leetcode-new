# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        # Base Case
        if head is None or head.next is None:
            return None

        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if slow != fast:
            return None
        
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
