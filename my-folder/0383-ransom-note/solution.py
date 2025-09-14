class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Approach 2 - slightly better space complexity wise
        hm = {}
        for c in magazine:
            hm[c] = 1 + hm.get(c, 0)
        
        for c in ransomNote:
            if c not in hm or hm[c] <= 0:
                return False
            hm[c] -= 1
        return True


        # Approach 1
        hm1 = {}
        hm2 = {}
        
        for c in ransomNote:
            hm1[c] = 1 + hm1.get(c, 0)
            
        for c in magazine:
            hm2[c] = 1 + hm2.get(c, 0)
        
        for ch, val in hm1.items():
            if ch not in hm2 or hm2[ch] < val:
                return False
        
        return True



