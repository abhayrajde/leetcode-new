class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1

        a, b = len(haystack), len(needle)
        for i in range(0, a - b + 1):
            if haystack[i] == needle[0] and i + b <= a and haystack[i:i+b] == needle:
                res = i
                break
        return res

        
