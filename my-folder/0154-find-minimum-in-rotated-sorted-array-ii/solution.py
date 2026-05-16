class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        resultInd = 0
        
        while l <= r:    
            # Avoid duplicates
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while r > l and nums[r] == nums[r - 1]:
                r -= 1
            
            mid = (l + r) // 2
            
            if nums[mid] < nums[resultInd]:
                resultInd = mid
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[resultInd]

