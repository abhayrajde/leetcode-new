class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            curr = []
            while n >= 10:
                remainder = n % 10
                curr.append(remainder)
                n = n // 10
            curr.append(n)
            res += reversed(curr)
        return res

        
