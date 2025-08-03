class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP: MEMOIZATION
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def dpmem(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if text1[i1] == text2[i2]:
                dp[i1][i2] = 1 + dpmem(i1 + 1, i2 + 1)
                return dp[i1][i2]
            opt1 = dpmem(i1, i2 + 1)
            opt2 = dpmem(i1 + 1, i2)
            dp[i1][i2] = max(opt1, opt2)
            return dp[i1][i2]
        return dpmem(0,0)

        # Recursion - Brute Force
        def recursion(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if text1[i1] == text2[i2]:
                return 1 + recursion(i1 + 1, i2 + 1)
            opt1 = recursion(i1, i2 + 1)
            opt2 = recursion(i1 + 1, i2)
            return max(opt1,opt2)
        return recursion(0,0)

