class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # two pointer approach, one pointer on word and another on abbr
        i = 0
        j = 0
        m = len(word)
        n = len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]: # if chars match, go forward
                i += 1
                j += 1
            elif abbr[j] == '0': return False # if we encounter 0 return False
            elif abbr[j].isnumeric(): # create int by looping all digits
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        
        return i == m and j == n


        # length = ""
        # for c in abbr:
        #     if c.isnumeric():
        #         if length == '' and c == '0': return False
        #         length += c
        #         continue

        #     if length:
        #         skipCount = int(length)
        #         if len(word) < skipCount:
        #             return False
        #         word = word[skipCount:]
        #         length = ""
        #     if word != '' and c == word[0]:
        #         word = word[1:]
        #     else:
        #         return False
        # if length and length[0] == '0': return False
        # if length == '':
        #     length = '0'
        # return length == '' or int(length) == len(word)

