class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
        is_special = set()

        for i in range(len(word)):
            if word[i].islower():
                lower_set.add(word[i])
            elif word[i].isupper():
                upper_set.add(word[i].lower())
            
            if word[i].lower() in lower_set and word[i].lower() in upper_set:
                is_special.add(word[i].lower())
        return len(is_special)

