class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        l1 = []
        while x >= 1:
            rem = x % 10
            l1.append(rem)
            x = x // 10
        
        l, r = 0, len(l1)-1
        while l <= r:
            if l1[l] != l1[r]:
                return False
            l += 1
            r -= 1
        return True

