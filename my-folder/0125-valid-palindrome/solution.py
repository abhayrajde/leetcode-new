class Solution:
    def isPalindrome(self, s: str) -> bool:
        contString = ''

        for i in range(len(s)):
            if s[i].isalnum():
                contString += s[i].lower()
        
        l, r = 0, len(contString)-1
        while l <= r:
            if contString[l] != contString[r]: return False
            l += 1
            r -= 1
        return True
