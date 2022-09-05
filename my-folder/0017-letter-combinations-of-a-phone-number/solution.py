class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        hm = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        self.curr = ""
        #23
        def backtrack(nums):
            if not nums:
                res.append(self.curr[:])
                return
            
            for j in hm[nums[0]]:
                self.curr+=j
        
                #some backtraking business performed here
                backtrack(nums[1:])
                
                self.curr = self.curr[:-1]
        backtrack(digits)
        return(res)
        """
        :type digits: str
        :rtype: List[str]
        """
        
