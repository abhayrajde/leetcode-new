class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            '1': '1',
            '0': '0',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        dup = ''
        for n in num:
            if n not in mapping:
                return False
            dup = mapping[n] + dup
        
        return num == dup
