
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        wordPtr = abbrPtr = 0

        while (wordPtr < len(word) and abbrPtr < len(abbr)):
            if abbr[abbrPtr].isdigit():
                steps = 0

                if abbr[abbrPtr] == "0":
                    return False

                while (abbrPtr < len(abbr) and abbr[abbrPtr].isdigit()):
                    steps = steps * 10 + int(abbr[abbrPtr])
                    abbrPtr += 1
                wordPtr += steps
            else:
                if word[wordPtr] != abbr[abbrPtr]:
                    return False

                wordPtr += 1
                abbrPtr += 1
        return wordPtr == len(word) and abbrPtr == len(abbr)
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
