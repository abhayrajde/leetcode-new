class Solution:
    def numDecodings(self, s: str) -> int:
        # DP - MEMOIZATION
        dp = [-1] * len(s)
        def dpmem(ind):
            if ind == len(s):
                return 1
            if ind > len(s):
                return 0
            if dp[ind] != -1:
                return dp[ind]
            
            opt1 = opt2 = 0
            if s[ind] != '0':
                opt1 = dpmem(ind+1)

            if s[ind] != '0' and int(s[ind:ind+2]) <= 26:
                opt2 = dpmem(ind + 2)
            dp[ind] = opt1 + opt2
            return dp[ind]
        return dpmem(0)
        
        #Recursion
        def recursion(ind):
            if ind == len(s):
                return 1
            if ind > len(s):
                return 0
            
            opt1 = opt2 = 0
            if s[ind] != '0':
                opt1 = recursion(ind+1)

            if s[ind] != '0' and int(s[ind:ind+2]) <= 26:
                opt2 = recursion(ind + 2)
            return opt1 + opt2
        return recursion(0)






        #this is only bottum up
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
