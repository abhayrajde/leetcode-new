# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head.next
        # find the median
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second part
        second = slow.next
        prev = slow.next = None
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        
        # Merge from both the sections
        first = head
        second = prev
        while(second):
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
