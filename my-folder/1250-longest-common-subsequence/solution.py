class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP: Tabulation
        dp = [[0]* (len(text2)+1) for i in range(len(text1) + 1)]
        for i1 in range(len(text1)-1, -1, -1):
            for i2 in range(len(text2)-1, -1, -1):
                if text1[i1] == text2[i2]:
                    dp[i1][i2] = 1 + dp[i1 + 1][i2 + 1]
                else:
                    dp[i1][i2] = max(dp[i1][i2 + 1], dp[i1 + 1][i2])
        return dp[0][0]


        
        # DP: Memoization - Top Down approach
        # TC - (N*M) | SC - O(N * M) + O(N + M)
        # O(N + M) - is an auxilary space - watch video for it.
        dp = [[-1]*len(text2) for i in range(len(text1))]
        def dpmem(i1, i2):
            # Base Case
            if i1 < 0 or i2 < 0:
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if text1[i1] == text2[i2]:
                dp[i1][i2] = 1 + dpmem(i1 - 1, i2 - 1)
                return dp[i1][i2]
            
            dp[i1][i2] = max(dpmem(i1 - 1, i2), dpmem(i1, i2 - 1))
            return dp[i1][i2]

        return dpmem(len(text1)-1, len(text2)-1)
        # def recursion(i1, i2):
        #     # Base Case
        #     if i1 < 0 or i2 < 0:
        #         return 0

        #     if text1[i1] == text2[i2]:
        #         return 1 + recursion(i1 - 1, i2 - 1)
        #     return max(recursion(i1 - 1, i2), recursion(i1, i2 - 1))
        # return recursion(len(text1)-1, len(text2)-1)

