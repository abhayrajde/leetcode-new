class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def recursion(openCt, closeCt):
            # Base Case
            if openCt == closeCt == n:
                res.append(''.join(stack))
                return

            if openCt < n:
                stack.append('(')
                recursion(openCt + 1, closeCt)
                stack.pop()
            
            if closeCt < openCt:
                stack.append(')')
                recursion(openCt, closeCt + 1)
                stack.pop()
        recursion(0,0)
        return res
            
            
        
