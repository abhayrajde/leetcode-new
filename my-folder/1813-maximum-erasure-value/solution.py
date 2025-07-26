class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        visited = set()
        currSum = 0

        while r < len(nums):
            if nums[r] not in visited:
                visited.add(nums[r])
                currSum += nums[r]
                res = max(res, currSum)
                r += 1       
            else:
                visited.remove(nums[l])
                currSum -= nums[l]
                l += 1
        return res

