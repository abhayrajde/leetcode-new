class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP MEMOIZATION - TOP DOWN APPROACH
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dpmem(i1,i2):
            # Base Case
            if (i1,i2) in dp:
                return dp[(i1,i2)]

            if i1 + i2 == len(s3):
                return True

            option1 = option2 = False
            if i1 < len(s1) and  s1[i1] == s3[i1 + i2]:
                option1 = dpmem(i1 + 1, i2)
            if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                option2 = dpmem(i1, i2 + 1)
            
            dp[(i1,i2)] = option1 or option2
            return dp[(i1,i2)]
        return dpmem(0,0)

        
        # RECURSION - BRUTE FORCE APPROACH
        def recursion(i1,i2, currPath):
            # Base Case
            if currPath == s3:
                return True
            
            option1 = option2 = False
            if i1 + 1 <= len(s1):
                option1 = recursion(i1 + 1, i2, currPath + s1[i1])
            if i2 + 1 <= len(s2):
                option2 = recursion(i1, i2 + 1, currPath + s2[i2])
            return option1 or option2
        return recursion(0,0,"")
            

        
