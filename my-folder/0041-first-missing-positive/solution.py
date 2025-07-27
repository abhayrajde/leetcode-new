class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # LOOP 1 - convert all negative to zero
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # LOOP 2 - for vals used in array: set the index to negative val
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # LOOP 3 - find first index with positive int
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
