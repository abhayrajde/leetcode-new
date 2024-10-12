class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = 0
        d = {0:1}
        ans = 0
        for num in nums:
            prev += num
            if prev-k in d:
                ans += d[prev-k]
            d[prev] = d.get(prev, 0) + 1
        return ans
