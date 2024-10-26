class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        word = ''
        for c in s:
            if c == ' ':
                if word:
                    output = word + ' ' + output
                    word = ''
                continue
            word += c

        if word:
            output = word + ' ' + output
        return output[:-1]
