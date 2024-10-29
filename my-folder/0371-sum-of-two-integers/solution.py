class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = pow(2, 32) - 1
        while b & mask:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a & mask if b > 0 else a
