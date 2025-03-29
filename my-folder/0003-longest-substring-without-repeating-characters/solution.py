class Solution(object):
    def lengthOfLongestSubstring(self, s):
        uset = set()
        maxCount = 0
        count = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in uset:
                uset.add(s[i])
                count += 1
                maxCount = max(maxCount, count)
            else:
                while s[j] != s[i]:
                    count -= 1
                    uset.remove(s[j])
                    j += 1
                uset.remove(s[j])
                uset.add(s[i])
                j += 1
        return maxCount
        """
        :type s: str
        :rtype: int
        """
        
