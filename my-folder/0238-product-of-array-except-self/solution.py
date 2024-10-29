class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        for i in range(1, len(nums)):
            n = nums[i-1]
            output.append(n * output[-1])
            
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * r
            r *= nums[i]

        return output
