class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        existing = set()
        while r < len(s):
            if s[r] not in existing:
                existing.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                existing.remove(s[l])
                l += 1
        return maxLen

