class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def traverse(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            if i == len(s) - 1: return 1

            res = traverse(i + 1)
            if int(s[i:i+2]) <= 26:
                res += traverse(i+2)
            return res

        return traverse(0)
