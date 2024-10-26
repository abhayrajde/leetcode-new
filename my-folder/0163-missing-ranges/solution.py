class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if lower == upper and len(nums) == 1:
            return []
        
        output = []
        
        for n in nums:
            if lower < n:
                output.append([lower, n - 1])
            
            lower = n + 1
        if lower <= upper:
            output.append([lower, upper])
        return output
