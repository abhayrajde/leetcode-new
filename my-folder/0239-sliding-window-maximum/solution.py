class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        q = collections.deque()     # monotonic decreasing queue - stores indexes 

        while r < len(nums):
            # Remove indexes of smaller values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # check if 1st element is q is out of bound
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
        return res
