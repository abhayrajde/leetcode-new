class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}

        for n in nums:
            if n in cache:
                return True
            cache[n] = True

        return False
