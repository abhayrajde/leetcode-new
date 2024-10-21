class Solution:
    digitmap = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    def myAtoi(self, s: str) -> int:
        isNegative = None
        nums = []
        for c in s:
            if c == ' ' and isNegative == None and len(nums) == 0:
                continue
            if (c == '-' or c == '+') and isNegative == None and len(nums) == 0:
                isNegative = c == '-'
                continue
            if c not in self.digitmap:
                break
            nums.append(self.digitmap[c])

        output = 0
        n = len(nums)
        for i in range(n):
            output += nums[i] * (10 ** (n - i - 1))
        
        if isNegative:
            output *= -1
        
        if output < (-2**31):
            return (-2**31)
        if output > (2**31 - 1):
            return (2**31 - 1)

        return output

    
