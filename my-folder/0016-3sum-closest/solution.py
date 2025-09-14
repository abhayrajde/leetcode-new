class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()

        for i in range(len(nums)):

            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if abs(currSum - target) < abs(res - target):
                    res = currSum

                if currSum > target:
                    r -= 1
                    
                elif currSum < target:
                    l += 1
                else:
                    return target
        return res


