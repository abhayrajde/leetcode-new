class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if lower == upper and len(nums) == 1:
            return []

        res = []
        for n in nums:
            if lower < n:
                res.append([lower, n - 1])
            lower = n + 1
        if lower <= upper:
            res.append([lower, upper])
        return res


