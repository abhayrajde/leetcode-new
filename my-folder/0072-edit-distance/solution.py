class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP MEMOIZATION - TOP DOWN APPROACH
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        def dpmem(i1, i2):
            if i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1):
                return len(word2) - i2
                
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            
            if word1[i1] == word2[i2]:
                dp[i1][i2] = dpmem(i1 + 1, i2 + 1)
            else:
                insert = 1 + dpmem(i1, i2 + 1)
                delete = 1 + dpmem(i1 + 1, i2)
                replace = 1 + dpmem(i1 + 1, i2 + 1)
                minops = min(insert, delete)
                minops = min(minops, replace)
                dp[i1][i2] = minops
            return dp[i1][i2]
        return dpmem(0,0)
        
        # RECURSION - BRUTE FORCE - TLE
        def recursion(i1, i2):
            if i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1):
                return len(word2) - i2
            
            if word1[i1] == word2[i2]:
                return recursion(i1 + 1, i2 + 1)
            else:
                insert = 1 + recursion(i1, i2 + 1)
                delete = 1 + recursion(i1 + 1, i2)
                replace = 1 + recursion(i1 + 1, i2 + 1)
                minops = min(insert, delete)
                minops = min(minops, replace)
                return minops
        return recursion(0,0)
