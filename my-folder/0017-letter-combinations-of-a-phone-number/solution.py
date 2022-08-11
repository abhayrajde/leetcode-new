class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        hm = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        res = []
        
        curr = ""
        
        def backtrack(digits,curr):
            if not digits:
                res.append(curr)
                return
            
            for i in hm[digits[0]]:
                backtrack(digits[1:],curr+i)
            
        backtrack(digits,curr)
        return(res)
                
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
