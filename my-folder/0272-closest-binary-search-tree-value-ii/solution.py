# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        min_heap = []

        def dfs(node):
            if not node:
                return

            heapq.heappush(min_heap, (abs(node.val - target), node.val))

            left = dfs(node.left)
            right = dfs(node.right)

        dfs(root)

        result = []
        for _ in range(k):
            diff, value = heapq.heappop(min_heap)
            result.append(value)
        return result


