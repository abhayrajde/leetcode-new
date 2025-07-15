class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        hm = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        def dfs(ind, curr):
            if ind >= len(digits):
                res.append("".join(curr[:]))
                return
            
            for j in hm[digits[ind]]:
                curr.append(j)
                dfs(ind + 1, curr)
                curr.pop()
            
        dfs(0, [])
        return res
        
