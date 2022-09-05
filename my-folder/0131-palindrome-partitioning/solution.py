class Solution(object):
    def partition(self, s):
        res = []
        curr = []
        def ispal(i,j):
            temp = s[i:j+1]
            if temp == temp[::-1]:
                return True
            return False
        
        def backtrack(ind):
            if ind >= len(s):
                res.append(curr[:])
                return
            for j in range(ind,len(s)):
                if ispal(ind,j):
                    curr.append(s[ind:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return res
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
