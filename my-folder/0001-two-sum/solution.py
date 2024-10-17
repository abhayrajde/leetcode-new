class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
    
        for i in range(len(nums)):
            n = nums[i]
            if n in cache: return [i, cache[n]]
            cache[target - n] = i

