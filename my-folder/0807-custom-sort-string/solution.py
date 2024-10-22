class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = {}

        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        output = ''
        for c in order:
            if c in counter:
                output += (c * counter[c])
                del counter[c]
        
        for c, n in counter.items():
            output += (c * n)

        return output
