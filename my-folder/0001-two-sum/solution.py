class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hm:
                return [hm[difference], i]
            hm[nums[i]] = i
