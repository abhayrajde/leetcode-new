# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            #reverse group
            prev, curr = nextGroup, prevGroup.next #twist here is we are not setting prev to null

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return dummy.next
    def getKth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

