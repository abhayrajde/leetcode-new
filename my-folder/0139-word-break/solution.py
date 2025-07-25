class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP - TABULATION - OPTIMIZED
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

        # DP - MEMOIZATION
        dp = {}
        def recursion(ind, currWord):
            if currWord == s:
                return True
            if ind >= len(wordDict):
                return False
            
            if (ind,currWord) in dp:
                return dp[(ind,currWord)]

            notPick = recursion(ind + 1, currWord) 
            pick = False
            cl, wl = len(currWord), len(wordDict[ind])
            if cl + wl - 1 < len(s) and s[cl: cl + wl] == wordDict[ind]:
                pick = recursion(0, currWord + wordDict[ind])
            
            dp[(ind,currWord)] = pick or notPick
            return dp[(ind,currWord)]
        
        return recursion(0, '')


        # RECURSION - BRUTE FORCE - TLE
        def recursion(ind, currWord):
            if currWord == s:
                return True
            if ind >= len(wordDict):
                return False
            
            notPick = recursion(ind + 1, currWord) 
            pick = False
            cl, wl = len(currWord), len(wordDict[ind])
            if cl + wl - 1 < len(s) and s[cl: cl + wl] == wordDict[ind]:
                pick = recursion(0, currWord + wordDict[ind])
            return pick or notPick
        return recursion(0, '')


