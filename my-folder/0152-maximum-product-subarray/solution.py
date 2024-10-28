class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        high = nums[0]
        low = nums[0]
        highest = high
        
        for num in nums[1:]:
            temp = max(num, max(high * num, low * num))
            low = min(num, min(high * num, low * num))

            high = temp
            highest = max(high, highest)
        
        return highest
