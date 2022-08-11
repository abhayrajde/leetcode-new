class Solution(object):
    def partition(self, s):
        res = []
        
        curr = []
        def ispal(s,i,j):
            temp = s[i:j+1]
            if(temp == temp[::-1]):
                return(True)
            return(False)
        
        def backtrack(i):
            if i>=len(s):
                res.append(curr[:])
                return
            
            for j in range(i, len(s)):
                if(ispal(s,i,j)):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return(res)
                    
            
        
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
