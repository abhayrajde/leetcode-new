class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = {}
        max_count, letter = 0, ''

        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
            if counter[c] > max_count:
                max_count = counter[c]
                letter = c
            if max_count > (len(s) + 1) // 2: return ''
        
        if len(counter) == len(s): return s

        output = [''] * len(s)
        i = 0
        while counter[letter] != 0:
            output[i] = letter
            i += 2
            counter[letter] -= 1
        
        for c, count in counter.items():
            while count > 0:
                if i >= len(s):
                    i = 1
                output[i] = c
                i += 2
                count -= 1
        return ''.join(output)
