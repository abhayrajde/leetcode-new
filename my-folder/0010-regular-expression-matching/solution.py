class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #DP MEMOIZATION - TOP DOWN APPROACH
        dp = {}
        def dpmem(i1,i2):
            if i1 >= len(s) and i2 >= len(p):
                return True
            
            if i2 >= len(p):
                return False

            if(i1, i2) in dp:
                return dp[(i1, i2)]

            if i2 + 1 < len(p) and p[i2 + 1] == '*':
                notTake = dpmem(i1, i2 + 2)
                take = False
                if i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.'):
                    take = dpmem(i1 + 1, i2)
                dp[(i1, i2)] = take or notTake
                return dp[(i1, i2)]

            if i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.'):
                dp[(i1, i2)] = dpmem(i1+1, i2+1)
                return dp[(i1, i2)]
            dp[(i1, i2)] = False
            return dp[(i1, i2)]

        return dpmem(0,0)

        # RECURSION - BRUTE FORCE APPROACH
        def recursion(i1,i2):
            if i1 >= len(s) and i2 >= len(p):
                return True
            
            if i2 >= len(p):
                return False

            if i2 + 1 < len(p) and p[i2 + 1] == '*':
                notTake = recursion(i1, i2 + 2)
                take = False
                if i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.'):
                    take = recursion(i1 + 1, i2)
                return take or notTake

            if i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.'):
                return recursion(i1+1, i2+1)
            return False
        return recursion(0,0)

