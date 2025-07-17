# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # This problem can also be solved using HashSet | TC - O(N), SC - O(N)
        # Better approach - Floyd's Tortoise & Hare Algo | TC - O(N), SC - O(1)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        
