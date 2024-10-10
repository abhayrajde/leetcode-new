class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length = ""
        for c in abbr:
            if c.isnumeric():
                if length == '' and c == '0': return False
                length += c
                continue

            if length:
                skipCount = int(length)
                if len(word) < skipCount:
                    return False
                word = word[skipCount:]
                length = ""
            if word != '' and c == word[0]:
                word = word[1:]
            else:
                return False
        if length and length[0] == '0': return False
        if length == '':
            length = '0'
        return length == '' or int(length) == len(word)

