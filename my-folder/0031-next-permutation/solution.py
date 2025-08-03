class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If we found a valid i, find the element to swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the elements from i + 1 to the end
        nums[i+1:] = nums[i+1:][::-1]
        # left, right = i + 1, len(nums) - 1
        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1
        
