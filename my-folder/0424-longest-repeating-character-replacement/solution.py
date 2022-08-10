class Solution(object):
    def characterReplacement(self, s, k):
        frequency = collections.defaultdict(int)
        startIndex = 0
        maxCharFreq = 0
        maxLength = 0
        
        for endIndex in range(len(s)):
            frequency[s[endIndex]] += 1
            maxCharFreq = max(maxCharFreq, frequency[s[endIndex]])
            while ((endIndex - startIndex + 1) - maxCharFreq) > k:
                frequency[s[startIndex]] -= 1
                startIndex += 1
            maxLength = max(maxLength, (endIndex - startIndex + 1))
            
        return maxLength
        
