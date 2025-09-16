class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            currCVal = (columnNumber - 1) % 26
            res = chr(ord('A') + currCVal) + res
            columnNumber = (columnNumber - 1) // 26
        return res
