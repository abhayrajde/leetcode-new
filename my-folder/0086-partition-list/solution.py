# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Time Complexity: O(N) 
        # Space Complexity: O(1)
        less_than_x = ListNode(0) # it will store all the elements less then x 
        greater_or_equal_to_x = ListNode(0) # all the elements equal to to greater than x

        less_than_x_pointer = less_than_x
        greater_or_equal_to_x_pointer = greater_or_equal_to_x

        curr = head

        while curr:
            if curr.val < x:
                less_than_x_pointer.next = curr
                less_than_x_pointer = less_than_x_pointer.next
            else:
                greater_or_equal_to_x_pointer.next = curr
                greater_or_equal_to_x_pointer = greater_or_equal_to_x_pointer.next
            curr = curr.next
        greater_or_equal_to_x_pointer.next = None
        less_than_x_pointer.next = greater_or_equal_to_x.next

        return less_than_x.next
