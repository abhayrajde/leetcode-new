class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = highest = nums[0]

        for n in nums[1:]:
            curr = max(n, curr + n)
            highest = max(highest, curr)
        
        return highest

