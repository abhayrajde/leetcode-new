class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # DP MEMOIZATION: TOP DOWN APPROACH
        dp = [[-1] * len(t) for _ in range(len(s))]
        def dpmem(i1, i2):
            # Base Cases
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            notPick = dpmem(i1 + 1, i2)
            pick = 0
            if s[i1] == t[i2]:
                pick = dpmem(i1 + 1, i2 + 1)
            dp[i1][i2] = pick + notPick
            return dp[i1][i2]
        return dpmem(0,0)
        
        # BRUTE FORCE APPROACH - TLE
        def recursion(i1, i2):
            # Base Cases
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0

            notPick = recursion(i1 + 1, i2)
            pick = 0
            if s[i1] == t[i2]:
                pick = recursion(i1 + 1, i2 + 1)
            return pick + notPick
        return recursion(0,0)



