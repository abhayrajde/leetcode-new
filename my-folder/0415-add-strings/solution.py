class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
            dic = {str(i): i for i in range(10)}
            if len(num1) > len(num2):
                num1, num2 = num2, num1
            n1 = len(num1)
            n2 = len(num2)
            c = 0
            output = ''
            for i2 in range(n2 - 1, -1, -1):
                i1 = i2 - (n2 - n1)
                d1 = 0 if i1 < 0 else dic[num1[i1]]
                d2 = dic[num2[i2]]
                tot = d1 + d2 + c
                c = 0
                if tot > 9:
                    c = 1
                    output = str(tot)[1] + output
                else:
                    output = str(tot) + output
            
            if c > 0:
                output = str(c) + output
            return output
