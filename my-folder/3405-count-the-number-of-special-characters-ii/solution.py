class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_low = defaultdict(int)
        first_up = defaultdict(int)


        specialCounter = 0

        for i in range(len(word)):
            if word[i].isupper():
                if word[i].lower() not in first_up:
                    first_up[word[i].lower()] = i
            else:
                last_low[word[i]] = i

        for c in last_low:
            if c in last_low and c in first_up and last_low[c] < first_up[c]:
                specialCounter += 1
        return specialCounter


