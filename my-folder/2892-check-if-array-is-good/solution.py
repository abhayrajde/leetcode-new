class Solution:
    def isGood(self, nums: List[int]) -> bool:
        counterMap = Counter(nums)
        numsLen = len(nums)
        for i in range(1, numsLen-1):
            if counterMap[i] != 1 or i not in counterMap:
                return False
        return counterMap[numsLen-1] == 2

        
        
