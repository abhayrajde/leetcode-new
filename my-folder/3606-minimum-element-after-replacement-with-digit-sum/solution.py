class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = float('inf')
        for i in range(len(nums)):
            temp = 0
            curr = nums[i]

            while curr > 0:
                remainder = curr % 10
                curr = curr // 10

                temp += remainder
            result = min(result, temp)
        return result
                

