class Solution:
    def numDecodings(self, s: str) -> int:
        # DP: Tabulation
        # TC: O(N) | SC: O(N)
        dp = [0] * (len(s) + 1)

        dp[len(s)] = 1
        for ind in range(len(s) - 1, -1, -1):
            opt1 = opt2 = 0
            if s[ind] != '0':
                opt1 += dp[ind + 1]
                if ind + 1 < len(s) and int(s[ind: ind + 2]) <= 26:
                    opt2 += dp[ind + 2]
            dp[ind] = opt1 + opt2
        return dp[0]

        # DP - Memoization
        # TC: O(N) | SC: O(N) + O(N) -> Auxilary/stack space
        dp = [-1] * len(s)
        def dpmem(ind):
            # Base conditions
            if ind == len(s): return 1
            if ind > len(s): return 0
            
            if dp[ind] != -1: return dp[ind]

            opt1 = opt2 = 0
            if s[ind] != '0':
                opt1 += dpmem(ind + 1)
                if ind + 1 < len(s) and int(s[ind: ind + 2]) <= 26:
                    opt2 += dpmem(ind + 2)
            
            dp[ind] = opt1 + opt2
            return dp[ind]
        return dpmem(0)
