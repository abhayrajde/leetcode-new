# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # 1. Move `prev` to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # 2. Reverse sublist [left, right]
        curr = prev.next
        prev_sublist = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_sublist
            prev_sublist = curr
            curr = nxt

        # 3. Reconnect
        prev.next.next = curr
        prev.next, prev = prev_sublist, prev.next

        return dummy.next
        
        # def findKth(node, k):
        #     curr = node
        #     prev = None
        #     while curr:
        #         if curr.val == k:
        #             return [prev, curr]
        #         prev = curr
        #         curr = curr.next
        #     return [prev, curr]

        # lprev, l = findKth(head, left)
        # rprev, r = findKth(head, right)
        # groupPrev = lprev
        # groupNext = r.next if r else None

        # # reverse list
        # prev, curr = groupNext, r
        # while curr != groupNext:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # groupPrev.next = prev
        # return head

