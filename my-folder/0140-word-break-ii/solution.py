class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dpmem(ind, currPath):
            if ind >= len(s):
                temp = ''
                for i in range(len(currPath)-1):
                    temp = temp + currPath[i] + ' '
                temp += currPath[-1]
                res.append(temp)
            
            for w in wordDict:
                if ind + len(w) <= len(s) and s[ind: ind + len(w)] == w:
                    dpmem(ind + len(w), currPath + [w])
        dpmem(0,[])

        return res
                
