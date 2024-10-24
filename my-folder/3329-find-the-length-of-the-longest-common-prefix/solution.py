class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = {}

        for n in arr1:
            while n not in prefixes and n > 0:
                prefixes[n] = 1
                n  = n // 10
        output = 0
        for n in arr2:
            while n > 0:
                if n in prefixes:
                    m = len(str(n))
                    if m > output:
                        output = m
                    break
                n  = n // 10
        return output
