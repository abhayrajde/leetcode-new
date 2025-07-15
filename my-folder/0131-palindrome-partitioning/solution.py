class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []
        
        def dfs(i):
            if i >= len(s):
                res.append(currPartition[:])
                return
                
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):
                    currPartition.append(s[i:j+1])
                    dfs(j + 1)
                    currPartition.pop()
        dfs(0)
        return res

    def isPali(self, s):
        if s == s[::-1]:
            return True
        return False
        
